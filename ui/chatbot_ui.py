import gradio as gr
import requests

API_BASE_URL = "http://188.121.119.22:8585"

def chat_with_bot(message, history):
    """
    Send a message to the chatbot API and receive a response.
    """
    if history is None:
        history = []
    try:
        # Prepare the request payload
        # Convert the Gradio history format to the API expected format
        api_history = []
        for user_msg, bot_msg in history:
            api_history.append({'HumanMessage': user_msg})
            api_history.append({'AIMessage': [bot_msg]})
        # Add the latest user message
        api_history.append({'HumanMessage': message})

        data = {
            "content": message,
            "content_type": "text",
            "url": "",
            "history": api_history
        }

        # Send the POST request to the /receive-message endpoint
        response = requests.post(f"{API_BASE_URL}/receive-message", json=data)
        response.raise_for_status()

        # Print the API response for debugging
        json_response = response.json()
        print("API Response:", json_response)

        # Extract the bot's reply from the API response
        bot_reply = ""
        if isinstance(json_response, list):
            for item in json_response:
                if 'AIMessage' in item:
                    ai_message_content = item['AIMessage']
                    if isinstance(ai_message_content, list) and len(ai_message_content) > 0:
                        bot_reply = ai_message_content[0]
                    elif isinstance(ai_message_content, str):
                        bot_reply = ai_message_content
                    else:
                        bot_reply = "Sorry, I couldn't understand the bot's reply."
                    break  # Exit the loop after finding the AIMessage
        else:
            bot_reply = "Sorry, I couldn't understand the response."

    except Exception as e:
        print("An error occurred in chat_with_bot:", e)
        bot_reply = "Sorry, I couldn't process your request."

    # Update the conversation history
    history.append((message, bot_reply))
    # Return the updated history and clear the message textbox
    return history, ""

def send_feedback(fact, type_value, tools_value, kw_value):
    """
    Send feedback to the chatbot API.
    """
    try:
        # Construct the metadata JSON
        metadata_json = {
            "tools": tools_value,
            "type": type_value,
            "kw": kw_value
        }

        data = {
            "fact": fact,
            "metadata": metadata_json
        }

        response = requests.post(f"{API_BASE_URL}/receive-feedback", json=data)
        response.raise_for_status()
        return "Feedback submitted successfully!"
    except Exception as e:
        print("An error occurred while sending feedback:", e)
        return "Failed to submit feedback."

with gr.Blocks() as demo:
    gr.Markdown("# ARITA")

    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(label="Chat with Bot", value=[])
            message = gr.Textbox(placeholder="Type your message here...", label="Your Message")
            send_button = gr.Button("Send")
            clear_button = gr.Button("Clear Chat")

            # Bind the send button to the chat_with_bot function
            send_button.click(
                chat_with_bot, 
                inputs=[message, chatbot], 
                outputs=[chatbot, message]
            )
            message.submit(
                chat_with_bot, 
                inputs=[message, chatbot], 
                outputs=[chatbot, message]
            )
            clear_button.click(lambda: [], None, chatbot, queue=False)

        with gr.Column(scale=1):
            gr.Markdown("## Send Feedback")
            feedback_text = gr.Textbox(placeholder="Enter your feedback here...", label="Feedback")
            type_dropdown = gr.Dropdown(
                choices=['video', 'audio', 'image'],
                label='Type'
            )
            tools_dropdown = gr.Dropdown(
                choices=['pika', 'suno', 'runway', 'pixverse', 'midjourney', 'luma', 'loudly', 'hailuo', 'flux'],
                label='Tools'
            )
            kw_input = gr.Textbox(placeholder="Enter keywords", label="KW")
            feedback_button = gr.Button("Submit Feedback")
            feedback_output = gr.Textbox(label="Feedback Status")

            # Bind the feedback button to the send_feedback function
            feedback_button.click(
                send_feedback,
                inputs=[feedback_text, type_dropdown, tools_dropdown, kw_input],
                outputs=feedback_output
            )


demo.launch()
