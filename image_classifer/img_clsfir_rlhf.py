import os
import getpass

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Provide your Google API Key")

import requests
from PIL import Image

def get_image(url, filename):
    content = requests.get(url).content
    with open(f'/content/{filename}.png', 'wb') as f:
        f.write(content)
    image = Image.open(f"/content/{filename}.png")
    image.show()
    return image

store_information = """
Nike Air Max Plus sneakers. They feature a brown upper with a black Nike Swoosh logo...
"""

from langchain import ChatGoogleGenerativeAI, ChatPromptTemplate, RunnablePassthrough

llm_vision = ChatGoogleGenerativeAI(model="gemini-pro-vision")
llm_text = ChatGoogleGenerativeAI(model="gemini-pro")

template = """
{context}
{information}
Provide brief information and store location.
"""
prompt = ChatPromptTemplate.from_template(template)

rag_chain = (
    {"context": retriever, "information": RunnablePassthrough()}
    | prompt
    | llm_text
)

full_chain = (
    RunnablePassthrough() | llm_vision | rag_chain
)

image = get_image("<image_url>", "sneaker")
message = HumanMessage(content=[{"type": "text", "text": "Provide information on Brand and model of given sneaker."}, {"type": "image_url", "image_url": image}])
result = full_chain.invoke([message])
print(result)


