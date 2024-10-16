import google.generativeai as genai
import random

def load_instructions(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

class ImageClassifier:
    def __init__(self, api_key, instructions_file='classification_instructions.txt'):
        self.api_key = api_key
        self.instructions = load_instructions(instructions_file)
        self.configure()

    def configure(self):
        genai.configure(api_key=self.api_key)

    def upload_image(self, file_path):
        return genai.upload_file(file_path)

    def classify_genre(self, image_file):
        instruction = random.choice(self.instructions)
        model = genai.GenerativeModel("gemini-1.5-pro")
        result = model.generate_content(
            [image_file, "\n\n", instruction]
        )
        return result.text

class GenreClassificationService:
    def __init__(self, classifier):
        self.classifier = classifier

    def classify_image(self, image_path):
        uploaded_image = self.classifier.upload_image(image_path)
        genre = self.classifier.classify_genre(uploaded_image)
        return genre
