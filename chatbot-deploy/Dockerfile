# Use the official chromadb image as a base
FROM chromadb/chroma:latest 

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that FastAPI will run on
EXPOSE 8585

# Command to run the FastAPI app using uvicorn
CMD ["uvicorn", "chatbot:app", "--host", "0.0.0.0", "--port", "8585"]

