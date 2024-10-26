import os

class Config:
    def __init__(self):
        self.GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
        file = open("instructions.txt", "r")
        self.INSTRUCT = file.read()
