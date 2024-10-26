'''
from flask import Flask, request, jsonify
from ai_model import AIModel
import google.generativeai as genai
import logging

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_media():
    file = request.files['file']
    logging.info('Uploading File...')
    _file = genai.upload_file(file.filename)
    logging.info('Uploading File Completed!')
    file_uri =  _file.uri
    mime_type = file.mime_type

    ai_model = AIModel()
    genre = ai_model.analyze_media(file_uri, mime_type)

    return jsonify({'genre': genre})

if __name__ == 'main':
    app.run()
'''

from flask import Flask, jsonify, request
from flask_restx import Api, Resource, reqparse, fields
import logging
import werkzeug
from ai_model import AIModel
import google.generativeai as genai


app = Flask(__name__)
api = Api(app)  # Initialize Flask-RESTX

# Define input and output models for API requests and responses
analysis_model = api.model('Analysis', {
    'file': fields.Raw(required=True, description='Media file to analyze'),
})

analysis_response_model = api.model('AnalysisResponse', {
    'genre': fields.String(required=True, description='Predicted genre of the media'),
})

# Configure request parser for handling file uploads
parser = reqparse.RequestParser()
parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files', required=True,
                    help='Media file to analyze')

@api.route('/analyze')
@api.expect(parser, validate=True)  # Validate request body
class AnalyzeMedia(Resource):
    @api.response(200, 'Analysis successful', analysis_response_model)
    @api.response(400, 'Bad request (e.g., missing file or invalid format)')
    @api.response(500, 'Internal server error')
    def post(self):
        logging.info('Uploading media file...')

        try:
            # Access uploaded file from request
            file = parser.parse_args()['file']

            # Use a robust mechanism for file uploads (consider cloud storage)
            
            logging.info(f'Uploading File {file.filename}')
            _file = genai.upload_file(file.filename)
            file_uri =  _file.uri
            mime_type = file.mime_type
            logging.info('Uploading file completed!')

            # Replace 'AIModel' with your actual media analysis function
            genre = analyze_media(file_uri, mime_type)  # Replace with your implementation

            return jsonify({'genre': genre}), 200
        except Exception as e:
            logging.error(f'Error during analysis: {e}')
            return {'message': 'An error occurred during analysis'}, 500

def analyze_media(file_uri, mime_type):
    # # Implement your specific media analysis logic here
    # # (e.g., using Tensorflow, PyTorch, or other AI frameworks)
    # # Leverage libraries like librosa for audio analysis or OpenCV for images
    # raise NotImplementedError('Implement your media analysis logic here')
    genai.configure(api_key='AIzaSyD7lveG7AUMh73mP4O53QKMI4ba8Ozk2Qc')
    ai_model = AIModel()
    genre = ai_model.analyze_media(file_uri, mime_type)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)