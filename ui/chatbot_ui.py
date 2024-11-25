import gradio as gr
import urllib3
import requests
from rich import print as rprint
API_BASE_URL = "http://188.121.119.22:8585"

def chat_with_bot(message, history):
    """
    Send a message to the chatbot API and receive a response.
    """
    if history is None:
        history = []
    # try:
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
        "content_type": "media",
        "url": "",
        "history": api_history
    }

    headers = {
        "Content-Type": "application/json",
        "accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    session = requests.Session()
    session.trust_env = False
    # Send the POST request to the /receive-message endpoint
    # response = urllib3.request(method='POST', url=f"{API_BASE_URL}/receive-message", json=data, headers=headers)
    response = session.post(f"{API_BASE_URL}/receive-message", json=data, headers=headers)
    # rprint(f"This is the req response: {response.json()}")
    # response.raise_for_status()

    # Print the API response for debugging
    json_response = response.json()[-1]
    print("API Response:", json_response)

    # Extract the bot's reply from the API response
    bot_reply = json_response['AIMessage'][0] if 'AIMessage' in json_response else 'متاسفم، نتوانستم درخواست شما را پردازش کنم.'

    # except Exception as e:
    #     # print("An error occurred in chat_with_bot:", e)
    #     raise e
    #     bot_reply = "متاسفم، نتوانستم درخواست شما را پردازش کنم."

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
        return "بازخورد با موفقیت ارسال شد!"
    except Exception as e:
        print("An error occurred while sending feedback:", e)
        return "ارسال بازخورد ناموفق بود."

with gr.Blocks() as demo:
    gr.Markdown("# آریتا")

    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(label="گفتگو با ربات", value=[])
            message = gr.Textbox(placeholder="پیام خود را اینجا وارد کنید...", label="پیام شما")
            send_button = gr.Button("ارسال")
            clear_button = gr.Button("پاک کردن گفتگو")

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
            gr.Markdown("## ارسال بازخورد")
            feedback_text = gr.Textbox(placeholder="بازخورد خود را اینجا وارد کنید...", label="بازخورد")
            type_dropdown = gr.Dropdown(
                choices=['video', 'audio', 'image'],  # Choices in English
                label='نوع'
            )
            tools_dropdown = gr.Dropdown(
                choices=['pika', 'suno', 'runway', 'pixverse', 'midjourney', 'luma', 'loudly', 'hailuo', 'flux'],  # Choices in English
                label='ابزارها'
            )
            kw_input = gr.Textbox(placeholder="کلمات کلیدی را وارد کنید", label="کلمات کلیدی")
            feedback_button = gr.Button("ارسال بازخورد")
            feedback_output = gr.Textbox(label="وضعیت بازخورد")

            # Bind the feedback button to the send_feedback function
            feedback_button.click(
                send_feedback,
                inputs=[feedback_text, type_dropdown, tools_dropdown, kw_input],
                outputs=feedback_output
            )

    # Set the direction to RTL
    demo.css = """
    body {
        direction: rtl;
    }
    """

    demo.launch()
