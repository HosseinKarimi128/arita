import gradio as gr
import requests

API_BASE_URL = "http://127.0.0.1:8585"

def chat_with_bot(message, history):
    if history is None:
        history = []

    # Convert Gradio history to the API format
    api_history = []
    for user_msg, bot_msg in history:
        api_history.append({'HumanMessage': user_msg})
        api_history.append({'AIMessage': [bot_msg]})
    api_history.append({'HumanMessage': message})

    data = {
        "content": message,
        "content_type": "media",
        "history": api_history
    }

    headers = {
        "Content-Type": "application/json",
        "accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.post(f"{API_BASE_URL}/receive-message", json=data, headers=headers)
    json_response = response.json()[-1]
    print("API Response:", json_response)

    bot_reply = json_response.get('AIMessage', ['متاسفم، نتوانستم درخواست شما را پردازش کنم.'])[0]
    history.append((message, bot_reply))

    return history, ""

def send_feedback(fact, type_value, tools_value, kw_value):
    try:
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

# ---------------------------
# Placeholder Generate Functions
# ---------------------------
def generate_image(prompt, tool):
    """
    Example function for generating images.
    Replace this with actual API call or logic.
    """
    return "https://via.placeholder.com/512x512.png?text=Generated+Image"

def generate_music(prompt, tool):
    """
    Example function for generating music.
    Replace this with actual API call or logic.
    """
    return "https://www.example.com/path-to-generated-music.mp3"

def generate_video(prompt, tool):
    """
    Example function for generating video.
    Replace this with actual API call or logic.
    """
    return "https://www.example.com/path-to-generated-video.mp4"


with gr.Blocks() as demo:
    gr.Markdown("# آریتا")

    # ------------------------
    # Row containing Chatbot & Tabs
    # ------------------------
    with gr.Row():
        # Left Column: Chatbot
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(label="گفتگو با ربات", value=[])
            message = gr.Textbox(
                placeholder="پیام خود را اینجا وارد کنید...", 
                label="پیام شما"
            )
            send_button = gr.Button("ارسال")
            clear_button = gr.Button("پاک کردن گفتگو")

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

        # Right Column: Tabs
        with gr.Column(scale=2):
            with gr.Tabs():
                # ----- Tab 1: تصویر -----
                with gr.Tab("تصویر"):
                    gr.Markdown("## تولید تصویر")
                    img_prompt = gr.Textbox(
                        placeholder="پرامپت تصویر خود را وارد کنید...",
                        label="پرامپت تصویر"
                    )
                    img_tool = gr.Dropdown(
                        choices=['pixverse', 'midjourney', 'runway'],
                        label="ابزار تولید تصویر"
                    )
                    generate_img_btn = gr.Button("تولید تصویر")
                    output_img = gr.Image(label="خروجی تصویر")

                    generate_img_btn.click(
                        generate_image,
                        inputs=[img_prompt, img_tool],
                        outputs=output_img
                    )

                # ----- Tab 2: موسیقی -----
                with gr.Tab("موسیقی"):
                    gr.Markdown("## تولید موسیقی")
                    music_prompt = gr.Textbox(
                        placeholder="پرامپت موسیقی خود را وارد کنید...",
                        label="پرامپت موسیقی"
                    )
                    music_tool = gr.Dropdown(
                        choices=['suno', 'loudly'],
                        label="ابزار تولید موسیقی"
                    )
                    generate_music_btn = gr.Button("تولید موسیقی")
                    output_music = gr.Audio(label="خروجی موسیقی")

                    generate_music_btn.click(
                        generate_music,
                        inputs=[music_prompt, music_tool],
                        outputs=output_music
                    )

                # ----- Tab 3: ویدیو -----
                with gr.Tab("ویدیو"):
                    gr.Markdown("## تولید ویدیو")
                    video_prompt = gr.Textbox(
                        placeholder="پرامپت ویدیو خود را وارد کنید...",
                        label="پرامپت ویدیو"
                    )
                    video_tool = gr.Dropdown(
                        choices=['runway', 'luma', 'flux'],
                        label="ابزار تولید ویدیو"
                    )
                    generate_video_btn = gr.Button("تولید ویدیو")
                    output_video = gr.Video(label="خروجی ویدیو")

                    generate_video_btn.click(
                        generate_video,
                        inputs=[video_prompt, video_tool],
                        outputs=output_video
                    )

    # ---------------------------------
    # Feedback Section Under Everything
    # ---------------------------------
    gr.Markdown("## ارسال بازخورد")
    feedback_text = gr.Textbox(placeholder="بازخورد خود را اینجا وارد کنید...", label="بازخورد")
    type_dropdown = gr.Dropdown(
        choices=['video', 'audio', 'image'], 
        label='نوع'
    )
    tools_dropdown = gr.Dropdown(
        choices=['pika', 'suno', 'runway', 'pixverse', 'midjourney', 'luma', 'loudly', 'hailuo', 'flux'],
        label='ابزارها'
    )
    kw_input = gr.Textbox(placeholder="کلمات کلیدی را وارد کنید", label="کلمات کلیدی")
    feedback_button = gr.Button("ارسال بازخورد")
    feedback_output = gr.Textbox(label="وضعیت بازخورد")

    feedback_button.click(
        send_feedback,
        inputs=[feedback_text, type_dropdown, tools_dropdown, kw_input],
        outputs=feedback_output
    )

    # Keep the RTL style
    demo.css = """
    body {
        direction: rtl;
    }
    """

    demo.launch()
