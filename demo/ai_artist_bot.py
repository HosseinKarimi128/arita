import logging
logger = logging.getLogger()
fhandler = logging.FileHandler(filename='mylog.log', mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage
from langchain.prompts import PromptTemplate
from typing import Optional, List
from chroma_client import chromaClient

class AIArtistBot:
    def __init__(self, openai_api_key: str, knowledge_dir: str):
        """
        Initialize the AI Artist chatbot
        
        Args:
            openai_api_key: API key for ChatGPT 3.5-turbo
            knowledge_dir: Directory containing knowledge base documents
        """
        self.llm = ChatOpenAI(model="gpt-3.5-turbo",api_key = openai_api_key)
        self.chroma_client = chromaClient("http://0.0.0.0:8324")
        
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
            template="""You are AI Artist, an expert in generating prompts for various multimedia generation tools.
            Use the following context and conversation history to generate an appropriate prompt.
            
            Context: {context}
            
            Chat History: {chat_history}
            
            Task Type: {task_type}
            User Request: {user_request}
            
            Generate a detailed prompt that:
            1. Incorporates relevant artistic styles and techniques from the context
            2. Uses appropriate tool-specific syntax and parameters
            3. Maintains consistency with the user's request
            4. Includes specific technical details (resolution, aspect ratio, etc.) when relevant
            
            Generated Prompt:"""
        )
    
    def generate_prompt(
        self,
        user_request: str,
        chat_history: list,
        task_type: str = "image",  # image, video, or music
        num_results: int = 1,
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
        # Retrieve relevant context
        docs = self.chroma_client.retrieve(
            query=user_request,
            k=3,
            # maximum_distance=0.4
        )
        context = "No context available." if docs is None else "\n".join([doc[0]["page_content"] for doc in docs])
        
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
    
    # def add_knowledge(self, text: str, source_name: str):
    #     """
    #     Add new knowledge to the bot's knowledge base
        
    #     Args:
    #         text: Text content to add
    #         source_name: Name/identifier for the source
    #     """
    #     # Split new content
    #     splitter = RecursiveCharacterTextSplitter(
    #         chunk_size=1000,
    #         chunk_overlap=200
    #     )
    #     splits = splitter.split_text(text)
        
    #     # Add to vector store
    #     self.vector_store.add_texts(splits)


# chatbot = AIArtistBot("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", "./chroma")
# print(chatbot.generate_prompt("Create a timelapse of a city from day to night",
#                               [HumanMessage(content="hi! The generator tool that I use, only understands pirate language"),
#                                 AIMessage(content="Ahoy! Sure I speak matey!")],
#                               "video"))
