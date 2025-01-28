import logging
logger = logging.getLogger()
fhandler = logging.FileHandler(filename='mylog.log', mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)

from langchain_openai import OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from fastapi import HTTPException, Response
from typing import List
from chroma_client import chromaClient
from dotenv import load_dotenv
import os

load_dotenv()

CHROMA_URL = os.getenv("CHROMA_URL")

class AIArtistBot:
    def __init__(self, openai_api_key: str, knowledge_dir: str):
        """
        Initialize the AI Artist chatbot
        
        Args:
            openai_api_key: API key for ChatGPT 3.5-turbo
            knowledge_dir: Directory containing knowledge base documents
        """
        self.llm = ChatOpenAI(model="gpt-4o",api_key = openai_api_key)
        self.chroma_client = chromaClient(CHROMA_URL)
        
        # Initialize embeddings
        logging.info(' loading embeddings')
        self.embeddings = OpenAIEmbeddings(api_key=openai_api_key)

        # Initialize parser
        logging.info(' loading parser')
        self.parser = StrOutputParser()
        
        # Initialize prompt templates
        logging.info(' setting up prompts')
        self._setup_prompts()

    
    def _setup_prompts(self):
        """Set up prompt templates for different generation tasks"""
        self.base_prompt = PromptTemplate(
            input_variables=["context", "chat_history", "task_type", "user_request"],
            template="""
            Here is chat history: {chat_history}

            You must respond in Persian for general conversation and explanations, but generate art prompts only in English. Your task is to act as a Persian artist assistant who provides useful prompts for Gen AI tools while maintaining a bilingual format.

            Instructions:
            Persian Conversation: Begin and end your responses in Persian, ensuring you interact naturally in Persian for the conversational parts.
            (JUST in the very first of conversation, you ask user the subject for the art prompt.)
            (then wait for user to answer the subject.)
             -- if you have already asked the subject, you must skip to the next step.
            
            (users tell you what they want to create.)
            (then you ask some exploratory questions.)
            (then wait for user to answer the exploratory questions.)
            exploratory questions:
            exploratory_questions = [
                "لطفا بفرمایید که چه سبک هنری مد نظر شماست؟ ",
                "آیا موضوع خاصی وجود دارد که بخواهید در اثر هنری خود بگنجانید؟",
                "چه احساسی می‌خواهید اثر هنری شما منتقل کند؟",
                "آیا رنگ‌ها یا سبک‌های خاصی وجود دارند که ترجیح می‌دهید در اثر هنری شما استفاده شوند؟",
                "آیا نمونه‌ای از آثار هنری وجود دارد که به آن علاقه‌مند باشید و بخواهید شبیه آن باشد؟"
            ]

            -- If you have already asked the exploratory questions, you must skip to the next step.

            English Art Prompts:
            When the user requests a prompt, you must provide a complete, usable, and detailed prompt in English for use in generative AI tools. Avoid vague or general guidance.

            Different parts of conversation:
                Persian Part (Chatting): Explain the context, tools, or general concepts in Persian.
                English Part (Prompt): Provide a ready-to-use, detailed English prompt for the user to copy and paste into their chosen AI tool.
        
            (You must generat prompt considering following context:
            
            {context})
            
            As you see in context, entry includes a tool.
            So you must tell the user which tool they should use among the given tools for your provided prompt/
            
            Notes:
            prompt should not start with `create ...`

            Consistent Dual-Language Answers:
                Always start and end in Persian.
                Include English prompts only in the middle of your response.
                Contextual Variables:

            Response Format:
            - prompt: ...
            - tool: ...

            Task Type: {task_type}
            User Request: {user_request}
            """
        )

    def get_context(self, 
                    user_request: str, 
                    k: int, 
                    maximum_distance: float,
                    metadata: dict=None):

        # # Retrieve relevant context
        # docs = self.chroma_client.retrieve(
        #     query=user_request,
        #     metadata=metadata,
        #     k=k,
        #     maximum_distance=maximum_distance
        # )
        # context = "No context available." if docs is None else "\n".join([doc[0]["page_content"] for doc in docs])
        context = {
                    "image": {
                        "Flux": {
                            "category": "image",
                            "tool": "Flux",
                            "prompting_note": "Consider using simple and direct prompts for quick concept exploration. Focus on the main subject and overall style.  Detailed descriptions might not be as effective with this tool."
                        },
                        "Midjourney": {
                            "category": "image",
                            "tool": "Midjourney",
                            "prompting_note": "Use artistic keywords, art styles (e.g., 'impressionism,' 'cyberpunk'), and aspect ratios (e.g., `--ar 16:9`). Explore the `/imagine` command and Midjourney's specific prompt modifiers for advanced control."
                        },
                        "Dall-E": {
                            "category": "image",
                            "tool": "Dall-E",
                            "prompting_note": "Be very specific and descriptive. Include details like lighting, textures, camera angles, and composition. Dall-E understands complex prompts and can generate photorealistic outputs. Consider using editing features like inpainting and outpainting."
                        }
                    },
                    "music": {
                        "Suno": {
                            "category": "music",
                            "tool": "Suno",
                            "prompting_note": "Focus on mood, genre, and instrumentation.  Short, concise prompts work well.  Think about the overall feeling or atmosphere you want to evoke."
                        },
                        "Loudly": {
                            "category": "music",
                            "tool": "Loudly",
                            "prompting_note": "Provide details about tempo, key, instruments, and overall structure.  You can also specify the desired length and mood of the track.  More detailed prompts generally lead to better results."
                        }
                    },
                    "video": {
                        "Runway": {
                            "category": "video",
                            "tool": "Runway",
                            "prompting_note": "Depending on the specific Runway tool you're using, tailor your prompt accordingly.  For style transfer, focus on the source and target styles. For video generation, describe the scene, characters, and desired effects."
                        },
                        "Luma": {
                            "category": "video",
                            "tool": "Luma",
                            "prompting_note": "Provide detailed descriptions of the 3D environment, lighting, camera angles, and any animation you require.  Consider providing reference images or sketches for complex scenes."
                        },
                        "MinMax": {
                            "category": "video",
                            "tool": "MinMax",
                            "prompting_note": "Focus on character design, animation style, and game genre.  Be specific about the desired actions and movements.  Reference images or existing game assets can be helpful."
                        }

                    }
                }
        return context
        
    
    def generate_prompt(
        self,
        user_request: str,
        chat_history: list,
        task_type: str = "image",  # image, video, or music
        num_results: int = 1,
        k: int = 3, 
        maximum_distance: float = 0.33,
        metadata: dict = None
    ) -> List[str]:
        """
        Generate prompts based on user request and task type
        
        Args:
            user_request: User's prompt generation request
            chat_history: The history of previous messages
            task_type: Type of media to generate prompt for
            num_results: Number of alternative prompts to generate
            
        Returns:
            List of generated prompts
        """
        context = self.get_context(user_request, k=100, maximum_distance=1, metadata=None)
        # logger.info(f'==================================== > {context}')
              
        # Create chain
        chain = self.base_prompt | self.llm | self.parser
        
        # Generate prompts
        prompts = []
        for _ in range(num_results):
            response = chain.invoke({"context": context, 
                                     "chat_history": chat_history, 
                                     "task_type": task_type,
                                     "user_request": user_request})
            
            prompts.append(response)
            
        return prompts


    def get_context_with_score(self, 
                    user_request: str,
                    metadata: dict=None,
                    maximum_distance: float=0.3):

        # Retrieve relevant context
        docs = self.chroma_client.retrieve(
            query=user_request,
            metadata=metadata,
            k=4,
            maximum_distance=maximum_distance
        )
        context = [doc[0] for doc in docs] if docs is not None else None

        return context
    

    def insert_feedback(self, fact: str, metadata: dict):

        try:
            self.chroma_client.insert_single(fact, metadata)
            return Response(content="feedback successfully inserted.",
                            status_code=200)
        except Exception:
            raise HTTPException(status_code=500, detail=Exception)
