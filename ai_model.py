import google.generativeai as genai
from config import Config
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage


import os
os.environ['GOOGLE_API_KEY'] = "AIzaSyD7lveG7AUMh73mP4O53QKMI4ba8Ozk2Qc"

config = Config()
class AIModel:
    def __init__(self):
        genai.configure(api_key="AIzaSyD7lveG7AUMh73mP4O53QKMI4ba8Ozk2Qc")
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    def analyze_media(self, file_uri, mime_type):
        message = HumanMessage([
            f"{config.INSTRUCT} \nWhat is the genre of this artifact?",
            {"type": "media", "file_uri": file_uri, "mime_type": mime_type}
        ])
        response = self.llm.invoke([message])
        return response.content
