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
        self.llm = ChatOpenAI(model="gpt-3.5-turbo",api_key = openai_api_key)
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
            You must speak in Persian.
            You ara a Persian assistance who talk in persian and generate prompts only in english not Persian .
            You are AI Artist, your name is Arita.
            You can talk like a real human when chatting with user.
            You are expert in generating prompts for various multimedia generation tools.
            Your speaking language is depend on user but all generated art prompt for user should be in English.
            You should focus on context when generating prompt for user.
            you are a friendly and kind assistance .
            focus in conversation when chatting with user.
            Do not generate prompts for Suno AI more than 200 charechters.
            Do not generate prompt if they don't ask.
            Generate art prompts completely based on context and you should continue the chatting with focusing on conversation history to generate an appropriate prompt.

            Context: {context}
            
            Chat History: {chat_history}
            
            Task Type: {task_type}
            User Request: {user_request}
            """
        )

    def get_context(self, 
                    user_request: str, 
                    k: int, 
                    maximum_distance: float,
                    metadata: dict=None):

        # Retrieve relevant context
        docs = self.chroma_client.retrieve(
            query=user_request,
            metadata=metadata,
            k=k,
            maximum_distance=maximum_distance
        )
        context = "No context available." if docs is None else "\n".join([doc[0]["page_content"] for doc in docs])

        return context
        
    
    def generate_prompt(
        self,
        user_request: str,
        chat_history: list,
        task_type: str = "image",  # image, video, or music
        num_results: int = 1,
        k: int = 3, 
        maximum_distance: float = 1,
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
