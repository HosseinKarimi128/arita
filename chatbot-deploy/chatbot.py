import logging
logger = logging.getLogger()
fhandler = logging.FileHandler(filename='mylog.log', mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)

from ai_artist_bot import AIArtistBot
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from fastapi import FastAPI, HTTPException, Response
from typing import Optional
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAIEmbeddings
from pathlib import Path
from langchain_openai import ChatOpenAI
import warnings
import requests
from dotenv import load_dotenv
import os
import openai

load_dotenv()


warnings.filterwarnings("ignore")


CHROMA_PATH = "./chroma"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
EMBEDDINGS = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
chatbot = AIArtistBot(OPENAI_API_KEY, CHROMA_PATH)
genai.configure(api_key=GOOGLE_API_KEY)


app = FastAPI(
  title="LangChain Chatbot",
  version="1.0",
  description="""A simple API server using LangChain's Runnable interfaces.
               This model must receive chat history and prepare the suitable response.""",
)


# descriptor = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
#     api_key=GOOGLE_API_KEY
# )


# Parser for JSON output
parser = JsonOutputParser()


class MessageRequest(BaseModel):
    content: str                           # Contains the prompt from user
    content_type: str                      # Contains the media type like image or music
    url: Optional[str] = None              # The raw URL of the attached file
    history: list[dict]                    # The history of the chat


class InsertRequestText(BaseModel):
    fact:  str                             # Contains the feedback
    metadata: Optional[dict] = None        # Metadata for each record in DB


def update_url(url: str):
    """ logic for transforming chat URL into server URI"""
    response = requests.get(url)
    response.raise_for_status()                     # Check for request errors
    content_type = response.headers.get('Content-Type', '')
    
    extension = content_type.split('/')[-1]         # e.g., "jpeg" for "image/jpeg"

    file_name = url.split("/")[-1].split("?")[0]    # Extract base name from URL

    if not file_name or '.' not in file_name:       # Handle cases with no filename or extension
        file_name = "downloaded_file"               # Default file name

    if not file_name.endswith(extension):           # Add extension if not already present
        file_name += f".{extension}"

    save_path = Path("temp_user_files") / file_name

    Path(save_path).parent.mkdir(parents=True, exist_ok=True)
    
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"File saved to {save_path}",'==============================================')
    _file = genai.upload_file(save_path)
        
    return _file.uri, _file.mime_type 



def update_history(human_message: str, ai_message: str, history: list):

    """logic for adding the last messages to history"""

    human_message = HumanMessage(content=human_message)
    ai_message = AIMessage(content=ai_message)

    history.append(human_message)
    history.append(ai_message)
    
    return history



def last_message_with_url(file_description, prompt: str):

    """Adds description to the last HumanMessage"""

    # prompt = prompt + f"\nHere is the description of the artifact: {file_description['desc']}"
    prompt = prompt + f"\nHere is the description of the artifact: {file_description}"
    return prompt


def format_history_to_json(messages: list[BaseMessage]) -> list[dict]:
    
    """Converts a list of LangChain Messages into a JSON-compatible format"""
    
    json_history = []
    for message in messages:

        if isinstance(message, HumanMessage):

            json_history.append({"HumanMessage": message.content})

        elif isinstance(message, AIMessage):

            json_history.append({"AIMessage": message.content})

        elif isinstance(message, BaseMessage):

            json_history.append({message.additional_kwargs.get("type", "BaseMessage"): message.content})
            
    
    return json_history



def format_history(chat_history: list[dict]):

    """logic for formatting the history from JSON to Chatbot format"""

    formatted_history = []
    for message in chat_history:

        if "HumanMessage" in message:
            formatted_history.append(HumanMessage(content=message["HumanMessage"]))

        elif "AIMessage" in message:
            formatted_history.append(AIMessage(content=message["AIMessage"]))

        else:
            formatted_history.append(BaseMessage(content=next(iter(message))))
    
    return formatted_history


# def describe_media(request: MessageRequest, formatted_history):
def describe_media(url):
    # def upload_file(file_path: str) -> dict:
    #     """Uploads a file to the specified URL and returns the server response."""
    #     with open(file_path, 'rb') as f:
    #         files = {'file': f}
    #         response = requests.post('https://tmpfiles.org/api/v1/upload', files=files)
    #     return response.json()['data']['url'].replace('tmpfiles.org/', 'tmpfiles.org/dl/')

    def create_payload(image_url: str) -> dict:
        return {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": [{"type": "text", "text": "You are a cool image analyst. Your goal is to describe what is in this image."}],
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What is in the image?"},
                        {"type": "image_url", "image_url": {"url": image_url}}
                    ]
                }
            ],
            "max_tokens": 500
        }

    def get_image_description(image_url: str, api_key: str) -> str:
        payload = create_payload(image_url)
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=payload)
        r = response.json()
        return r["choices"][0]["message"]["content"]
    # image_url = upload_file(url)

    response = get_image_description(url, OPENAI_API_KEY)

    return response


    # system_template = """You are a user assistant that takes prompts from users and analyzes the files such as images, musics and videos.
    #                  Please note that:
    #                  1- You should output only one field 'desc' in JSON format.
    #                     The 'desc' is your own description of the file (in bullet points and not sentences).
    #                     Your must describe it like an artist and include all informations like genre and different aspects.
    #                  2- The description must be generated considering the user prompts and the chat history.
    #                  3- User prompts must not include politics, adult content or violence.
    #                  4- If the user prompts doesn't describe the file, do not consider it in your description
    #                  5- In the 'desc' that you create, use less verbs and make it small phrases.
                     
    #                  Example: 
    #                     a. The user uploads a scene of Blade Runner 2049.
    #                        User sends this prompt: 'I am pretty sure this image is AI-generated'
    #                        and you describe it like 'desc' : ['cyberpunk', 
    #                        'AI-generated', 'sci-fi'] and more.
    #                     b. The user uploads a music of Metallica.
    #                        User sends this prompt: 'I want a music like this!'
    #                        and you describe it like 'desc' : ['Heavy Metal', 'consisted of electric guitars, bass and drums', 'heavy distortion'] and more.
    #                 \n\n
    #                 """

    # prompt_template = ChatPromptTemplate.from_messages([
    #     ("system", system_template),
    #     MessagesPlaceholder("chat_history"),
    #     HumanMessage(content=[
    #         request.content, 
    #         {
    #         "type": "media",
    #         "file_uri": request.url,
    #         "mime_type": request.content_type,
    #         }
    #     ])
    # ])

    # file_description_chain = prompt_template | descriptor | parser

    # response = file_description_chain.invoke({"chat_history": formatted_history})
    
    return response
    


@app.post("/receive-message")
async def receive_message(request: MessageRequest):
    if not request.content:
        raise HTTPException(status_code=400, detail="User message cannot be empty")

    formatted_history = format_history(request.history)
    last_human_message = request.content

    if request.url:
        print(request.url)
        description = describe_media(request.url)
        last_human_message = last_message_with_url(description, request.content)
    logger.info(request.content_type.split('/')[-1])
    response = chatbot.generate_prompt(
        user_request=last_human_message,
        chat_history=formatted_history,
        task_type=request.content_type.split('/')[-1],
        num_results=1
    )

    updated_history = update_history(last_human_message, response, formatted_history)
    formatted_history = format_history_to_json(updated_history)

    return formatted_history




@app.post("/receive-feedback")
async def receive_feedback(request: InsertRequestText):

    ## TODO later: Feedback may not be informative, so adding logic of data extraction

    results = chatbot.get_context_with_score(request.fact, request.metadata, 0.2)
    
    if results is None:
        return chatbot.insert_feedback(request.fact, request.metadata)
    else:
        return Response(status_code=204)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8585, reload=True)
