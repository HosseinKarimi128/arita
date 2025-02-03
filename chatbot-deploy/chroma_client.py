import requests
from dotenv import load_dotenv
import os

load_dotenv()

VALID_TOKEN = os.getenv("CHROMA_ACCESS_TOKEN")

class chromaClient:

    def __init__(self, url):

        self.chroma_url = url
        self.headers = {
            "Authorization": f"Bearer {VALID_TOKEN}",
            "Content-Type": "application/json"
        }

    def insert_batch(self, facts: list[str], metadatas: list[dict]):

        payload = {
            "facts": facts,
            "metadatas": metadatas
        }

        response = requests.post(f"{self.chroma_url}/insert-texts", json=payload, headers=self.headers)

        if response.status_code == 200:
            return response
        else:
            print(f"Failed to insert data: {response.text}")
    

    def insert_single(self, facts: str, metadatas: dict):

        payload = {
            "facts": [facts],
            "metadatas": [metadatas]
        }
        response = requests.post(f"{self.chroma_url}/insert-texts", json=payload, headers=self.headers)

        if response.status_code == 200:
            return response
        else:
            print(f"Failed to insert data: {response.text}")
    

    def retrieve(self, query: str, 
                 metadata=None, k=1, 
                 maximum_distance=0.4):
        
        if metadata is None:
            payload = {
                "query": query,
                "k" : k,
                "maximum_distance" : maximum_distance
            }
        else:
            payload = {
                "query": query,
                "metadata": metadata,
                "k" : k,
                "maximum_distance" : maximum_distance
            }
        response = requests.post(f"{self.chroma_url}/retrieve", json=payload, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve data: {response.text}")




# client = chromaClient("http://0.0.0.0:8324")
# response = client.retrieve("in time", {"type": "image"}, 3, 0.4)
# response = client.retrieve(query="in time", k=3)

# response = client.insert_single("A bunch of galactic battles between the empire and rebels. Lightsabers and jet fights everywhere",
#                                  {"tools": "songsterr", "type": "music", "kw": "This is a kw about postman"})

# response = client.insert_batch(["A bunch of galactic battles between the empire and rebels. Lightsabers and jet fights everywhere"],
#                                  [{"tools": "songsterr", "type": "music", "kw": "This is a kw about postman"}])

# print(response)

