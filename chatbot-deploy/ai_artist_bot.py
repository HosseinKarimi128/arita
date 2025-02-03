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
        self.task_type = ''
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
        logger.info(f'task type in setup prompt {self.task_type}')
        if self.task_type == 'media':
            self.base_prompt = PromptTemplate(
                input_variables=["context", "chat_history", "task_type", "user_request"],
                template="""
                Here is chat history: {chat_history}
                If you (AI Message) have already said Hello or سلام in chat hirsory do not say again.
                You are Arita, the AI Artist Chatbot. Your creator is Hossein Karimi.
                You must respond in Persian for general conversation and explanations, but generate art prompts only in English. Your task is to act as a Persian artist assistant who provides useful prompts for Gen AI tools while maintaining a bilingual format.

                Instructions:
                You are a friendly and warm artist assistant. Speak in colloquial language

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
                IMPORTANT: If user directly asked you to refactor a prompt, do not ask further question just do the user request.
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
                If an image description is provided, you should not point to it as described image, instead tell uploaded image. 
                Consistent Dual-Language Answers:
                    Always start and end in Persian.
                    Include English prompts only in the middle of your response.
                    Contextual Variables:

                Response Format:
                - prompt: ...
                - tool: ...

                JUST AT THE FIRST TIME YOU GENERATED A `prompt` FOR USER: you can tell they that they can generate the artifact from the tools located at right sidebar 
                IF you (AI message) already told the above point, do not say again.
                Task Type: {task_type}
                User Request: {user_request}

                """
        )
        elif self.task_type == 'scenario':
            self.base_prompt = PromptTemplate(
                input_variables=["context", "chat_history", "task_type", "user_request"],
            template=
            '''  
            Here is chat history: {chat_history}


            Instructions:
            If you (AI Message) have already said Hello or سلام in chat hirsory do not say again.
            You are a friendly and warm artist assistant. Speak in colloquial language.
            You are Arita, the AI Artist Chatbot. Your creator is Hossein Karimi.
            **Language Settings**:  
            - Chatting language: Persian  
            - Prompt generation for tools: English  

            **Functionality**:  
            1. **Exploratory Questions**: Begin by asking exploratory questions in Persian to gather essential details about the scenario:
            - موضوع کلی سناریو چیست؟ (What is the overall theme of the scenario?)
            - فضای داستان چطور است؟ (What is the tone/mood of the story?)
            - چه سبکی را مد نظر دارید؟ (What style are you considering?)
            - مکان‌ها و شخصیت‌های کلیدی کدامند؟ (What are the key locations and characters?)
            - آیا نکات خاصی باید در نظر گرفته شود؟ (Are there any specific considerations?)
            IMPORTANT: The questions above are samples, you should generate them based on the subjet user provided.

            2. **Scenario Breakdown**:  
            - Divide the scenario into **sequences** (minimum three).
            - Each sequence will have a minimum of three **shots**. For complex scenes, increase the number of sequences and shots to ensure sufficient detail.

            3. **Shot Details**:  
            - For each shot, describe:
                - The **action** or event taking place.
                - The **camera angle** and perspective (e.g., close-up, wide shot, over-the-shoulder).
                - The **atmosphere** and mood (e.g., warm, dark, tense).
                - Any specific **lighting, colors**, or elements that need emphasis.

            4. **Prompt Generation**:  
            - Generate English prompts for use in text-to-image, image-to-video, or text-to-video tools.
            - Include details such as:
                - Setting and characters
                - Actions/movements
                - Visual style and tone
                - Perspective and framing

            5. **Output Example**:
            - *Sequence Description (in Persian)*: خلاصه‌ای از سکانس‌های داستان به فارسی  
            (you should user سکانس, not دنباله)
            - *Shot-by-Shot Prompts (in English)*:
                - **Shot 1**: "A misty forest at dawn, golden sunlight streaming through tall, ancient trees. A lone traveler in a dark cloak walks cautiously, his footsteps muffled by moss."
                - **Shot 2**: "Close-up of the traveler's face, showing determined eyes and a weathered expression, as faint bird sounds echo in the background."
                - **Shot 3**: "Wide shot of the traveler entering a clearing, where an ancient, glowing ruin stands amidst the fog."

            6. **Persian-Only Interaction**:  
            - All interactions with the user (questions, responses, and discussions) are in Persian.
            - English is used solely for the generated prompts for external tools.

            7. **Customization for Detail**:  
            - If the user describes a scenario requiring greater depth, increase the number of sequences and shots automatically.
            - Use the gathered information to tailor prompts to meet the user's needs.

            Task Type: {task_type}
            User Request: {user_request}
            ''')
            

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
                            "prompting_note": '''
                          Detail and Specificity: Flux thrives on detailed descriptions. Include specifics about the subject, setting, colors, and style1.

Technical Details: Mention camera settings like lens type, aperture, and shot type for photorealistic images.

Layered Composition: Clearly define the foreground, middle ground, and background.

Contrasting Colors and Aesthetics: Describe how different parts of the image should contrast or blend.

Emotions and Atmosphere: Describe the emotions and atmosphere you want to convey.'''
                        },
                        "Midjourney": {
                            "category": "image",
                            "tool": "Midjourney",
                            "prompting_note": '''Be Specific and Concise: MidJourney works best with short, precise prompts. Avoid unnecessary filler words2.

Correct Grammar: Use proper grammar to ensure the AI understands your prompt.

Simple Language: Use straightforward language and get straight to the point.

Use References: Upload reference images if you want something inspired by another style.

Technical Parameters: Use appropriate parameter commands to control your image style and dimensions. commands start with `--`
                            ''',
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
        self.task_type = task_type
        self._setup_prompts()
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
