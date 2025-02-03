# Arita AI Chatbot

## Overview
Arita is an AI-powered chatbot designed to assist users in generating prompts for various artistic tools, including image, video, and music generation. It is built using FastAPI and LangChain, integrating OpenAI and Google AI models to enhance user interactions and media generation.

## Features
- **Conversational AI**: Supports Persian (Farsi) for general conversation and English for artistic prompt generation.
- **Multi-Modal Support**: Handles text, image, and audio input.
- **Context-Aware Responses**: Uses a ChromaDB vector store for enhanced response retrieval.
- **AI Image Analysis**: Describes uploaded images and integrates with generative AI tools.
- **User Feedback Integration**: Stores user feedback for future improvements.

## Project Structure
```
├── chatbot-deploy/         # Main chatbot service
│   ├── ai_artist_bot.py   # Chatbot logic and AI model integration
│   ├── chatbot.py         # FastAPI application for handling chat interactions
│   ├── chroma_client.py   # Client for interacting with ChromaDB
│   ├── Dockerfile         # Containerization file for chatbot service
│   ├── .env               # Environment variables for API keys
│   ├── requirements.txt   # Python dependencies
│
├── chroma-server.py       # ChromaDB server
├── image_classifier/      # Image classification module
│   ├── app.py             # FastAPI application for image classification
│   ├── image_classifier_instructions.py  # Image classification logic
│
├── ui/                    # Chatbot UI with Gradio
│   ├── chatbot_ui.py      # User interface for interacting with the chatbot
│
├── docker-compose.yml     # Docker compose file for running services
├── Dockerfile             # Main Dockerfile for ChromaDB
├── README.md              # Project documentation
```

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- **Docker** and **Docker Compose**
- **Python 3.9+** (if running locally)

### Environment Variables
Create a `.env` file with the required API keys:
```
OPENAI_API_KEY=your-openai-api-key
GOOGLE_API_KEY=your-google-api-key
CHROMA_ACCESS_TOKEN=your-chroma-access-token
CHROMA_URL=http://chroma-server:8324
```

### Running with Docker
To start all services using Docker Compose, run:
```sh
docker-compose up --build -d
```
This will spin up:
- **ChromaDB** on port `8324`
- **Chatbot API** on port `8585`

### Running Locally
To run the chatbot without Docker:
```sh
cd chatbot-deploy
pip install -r requirements.txt
uvicorn chatbot:app --host 0.0.0.0 --port 8585
```
To start ChromaDB:
```sh
python chroma-server.py
```

## API Endpoints
### Chatbot API (`8585`)
- **`POST /receive-message`** - Handles user messages and generates prompts.
- **`POST /receive-feedback`** - Stores user feedback for model improvement.

### ChromaDB API (`8324`)
- **`POST /insert-texts`** - Inserts knowledge into ChromaDB.
- **`POST /retrieve`** - Retrieves relevant knowledge based on user queries.

## UI Access
The chatbot UI (Gradio) can be accessed by running:
```sh
python ui/chatbot_ui.py
```
This will launch a browser-based chat interface.

## Usage
1. Start a conversation with Arita in **Persian**.
2. Request an art prompt, and Arita will generate an English prompt for AI tools.
3. Upload an image, and Arita will describe it before refining a related prompt.
4. Generate images, music, or videos using the available tools in the UI.

## Troubleshooting
- If the chatbot does not respond, check if ChromaDB is running (`docker ps`).
- Ensure `.env` contains valid API keys.
- Check logs using:
  ```sh
  docker logs arita-demo
  ```
## License
This project is licensed under the **GNU GENERAL PUBLIC LICENSE**.

