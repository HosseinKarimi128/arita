import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from rich import print as rprint
CHROMA_PATH = "./chroma"
OPENAI_TOKEN = os.getenv("OPENAI_API_KEY")
VALID_TOKEN = os.getenv("CHROMA_ACCESS_TOKEN")
EMBEDDINGS = OpenAIEmbeddings(api_key=OPENAI_TOKEN)
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=EMBEDDINGS)
rprint(db.get())