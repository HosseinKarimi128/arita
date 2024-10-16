import os
from flask import Flask
from flask_restx import Api, Resource, fields
from werkzeug.datastructures import FileStorage
from image_classifier_instructions import ImageClassifier, GenreClassificationService

app = Flask(__name__)
api = Api(app, version='1.0', title='Image Genre Classification API',
          description='A simple API to classify the genre of an image')

# Initialize the service
api_key = "AIzaSyD7lveG7AUMh73mP4O53QKMI4ba8Ozk2Qc"
classifier = ImageClassifier(api_key)
service = GenreClassificationService(classifier)

# Define the expected input payload
upload_parser = api.parser()
upload_parser.add_argument('image', location='files',
                           type=FileStorage, required=True)

# Define the response model
genre_model = api.model('Genre', {
    'genre': fields.String(description='The classified genre of the image')
})

@api.route('/classify')
class ImageClassification(Resource):
    @api.expect(upload_parser)
    @api.response(200, 'Success', genre_model)
    @api.response(400, 'Validation Error')
    def post(self):
        """Classify the genre of an uploaded image"""
        args = upload_parser.parse_args()
        image_file = args['image']

        if image_file.filename == '':
            api.abort(400, "No image file provided")

        # Save the uploaded file temporarily
        temp_path = "temp_image.png"
        image_file.save(temp_path)

        try:
            genre = service.classify_image(temp_path)
            return {'genre': genre}, 200
        except Exception as e:
            api.abort(500, f"An error occurred: {str(e)}")
        finally:
            # Clean up the temporary file
            if os.path.exists(temp_path):
                os.remove(temp_path)

if __name__ == "__main__":
    app.run(debug=True)
