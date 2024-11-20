from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from config import Config
import os
from langchain_core.messages import HumanMessage, SystemMessage

os.environ['GOOGLE_API_KEY'] = "AIzaSyD7lveG7AUMh73mP4O53QKMI4ba8Ozk2Qc"
os.environ['OPENAI_API_KEY'] = "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"
config = Config()


class AIModel:
    def __init__(self):

        genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
        loader = TextLoader("context.txt")
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings(api_key=os.environ['OPENAI_API_KEY'])
        vector_store = FAISS.from_documents(docs, embeddings)
        retriever = vector_store.as_retriever()
        qa_chain = ConversationalRetrievalChain.from_llm(llm = self.llm, retriever=retriever)
        chat_history = []
        while True:
            query = input()
            result = qa_chain({"question": query, "chat_history": chat_history})
            chat_history.append((query, result["answer"]))
    
    def analyze_media(self, file_uri, mime_type):

        message = SystemMessage([
            config.INSTRUCT
        ])
        message = HumanMessage([
            {"type": "media", "file_uri": file_uri, "mime_type": mime_type}
        ])
        response = self.llm.invoke([message])
        return response.content