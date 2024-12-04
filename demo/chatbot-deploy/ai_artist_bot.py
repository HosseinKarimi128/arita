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
        self.llm = ChatOpenAI(model="gpt-4o-mini",api_key = openai_api_key)
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
            You ara a Persian artist assistance who talk in Persian and generate useful art prompts only in English not Persian .
            For example: 
                if user said: " می خواهم یک عکس تولید کنم"
                you should respond: "برای تولید عکس میتوانید از ابزارهای فلان و فلان استفاده کنید. این یک پرامپت برای تولید تصویر در ابزار فلان:
                'This is a sample prompt in English' شما می توانید از این پرامپت برای استفاده در فلان ابزار استفاده کنید."
            SO: your answeres should have two parts: Chatting part - that should be in Persian - and Prompt Part - that should be in English.
            SO: your answeres have both Persian parts and English Parts. The english parts are the prompts that users should use in GenAI tools, and the Persian parts are about just chatting with user.
            Your primary language is Persian, BUT when you want to generate prompts to use in Gen AI tools you should genrate it in English
            SO: You answeres should not be fully Persian or fully english. 
            You answeres starts with Persian language and also ends with Persian language.
            Note that: the generate prompt should NOT be just facts about generating prompts, they should acutally be a usable prompt so user can copy and paste then in tools
                    for example:
                        this is a bad prompt: 'Include romantic themes and emotional melodies to create a heartfelt composition.'
                        this is a good prompt: 'A love pop song in E minor with bpm of 120 with verse-chours-verse-chours-outro structure with acoustic guitar and piano with some mello drums , have a happy theme and romantic atmosphere .

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
