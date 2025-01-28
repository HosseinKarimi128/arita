import gradio as gr
import requests
import random
import base64
import requests
from io import BytesIO
from PIL import Image

API_BASE_URL = "http://127.0.0.1:8585"

def upload_image(file):
    """
    Uploads the image to a temporary file hosting service and returns the URL.
    You can replace this function with your preferred image hosting service.
    """
    if file is None:
        return None

    try:
        with open(file.name, "rb") as f:
            files = {'file': f}
            response = requests.post('https://tmpfiles.org/api/v1/upload', files=files)
            response.raise_for_status()
            return response.json()['data']['url'].replace('tmpfiles.org/', 'tmpfiles.org/dl/')
    except Exception as e:
        print("Error uploading image:", e)
        return None

def chat_with_bot(message, image, content_type, history):
    if history is None:
        history = []

    # Handle image upload
    image_url = None
    if image is not None:
        image_url = upload_image(image)
        if image_url is None:
            bot_reply = "متاسفم، نتوانستم تصویر شما را بارگذاری کنم."
            history.append((message, bot_reply))
            return history, ""

    # Convert Gradio history to the API format
    api_history = []
    for user_msg, bot_msg in history:
        api_history.append({'HumanMessage': user_msg})
        api_history.append({'AIMessage': [bot_msg]})
    
    # Prepare the data payload
    data = {
        "content": message,
        "content_type": content_type,
        "history": api_history
    }

    # Include the image URL if available
    if image_url:
        data["url"] = image_url

    headers = {
        "Content-Type": "application/json",
        "accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.post(f"{API_BASE_URL}/receive-message", json=data, headers=headers)
        response.raise_for_status()
        json_response = response.json()[-1]
        print("API Response:", json_response)

        bot_reply = json_response.get('AIMessage', ['متاسفم، نتوانستم درخواست شما را پردازش کنم.'])[0]
        history.append((message, bot_reply))
    except requests.exceptions.RequestException as e:
        print("Request error:", e)
        bot_reply = "خطا در ارتباط با سرور. لطفاً بعداً تلاش کنید."
        history.append((message, bot_reply))
    except Exception as e:
        print("Unexpected error:", e)
        bot_reply = "خطای غیرمنتظره رخ داده است."
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
def generate_image(
    prompt,
    tool,  # Not used here, but included for consistency
    width=720,
    height=1024,
    num_steps=24,
    guidance=3.5,
    seed=None,
    strength=1.0,
    init_image=None  # base64 or path to an image
):
    """
    Generate an image by calling an API endpoint that returns raw JPEG bytes.
    The function returns a PIL Image, which Gradio can display directly 
    via gr.Image(...).
    """

    # If no seed is provided, generate one randomly
    if seed is None:
        seed = random.randint(0, 9999999)

    # Build the request payload
    payload = {
        "prompt": prompt,
        "width": width,
        "height": height,
        "num_steps": num_steps,
        "guidance": guidance,
        "seed": seed,
        "strength": strength
    }

    # If you have an init_image, either pass it as base64 directly
    # or read from a file and encode it to base64
    if init_image is not None:
        payload["init_image"] = init_image

    try:
        response = requests.post(
            "http://46.34.167.8:8088/generate",
            json=payload,
            stream=True
        )
        response.raise_for_status()

        image_bytes = response.content
        image = Image.open(BytesIO(image_bytes))

        return image

    except requests.exceptions.RequestException as e:
        print("Request error:", e)
        return "https://via.placeholder.com/512.png?text=Error"

    except Exception as e:
        print("Error generating image:", e)
        return "https://via.placeholder.com/512.png?text=Unexpected+Error"

def generate_music(prompt, tool):
    return "https://www.example.com/path-to-generated-music.mp3"

def generate_video(prompt, tool):
    return "https://www.example.com/path-to-generated-video.mp4"

css = """
.rtl-textbox{
  text-align: right;
}
"""

with gr.Blocks(theme="soft", css=css) as demo:
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
                label="پرامپت شما"
            )
            content_type_dropdown = gr.Dropdown(
                choices=['media', 'scenario'], 
                label="نوع محتوا",
                value='media'
            )
            image_upload = gr.File(
                label="آپلود تصویر", 
                file_types=["image"]
            )
            send_button = gr.Button("ارسال")
            clear_button = gr.Button("پاک کردن گفتگو")

            send_button.click(
                chat_with_bot,
                inputs=[message, image_upload, content_type_dropdown, chatbot],
                outputs=[chatbot, message]
            )
            message.submit(
                chat_with_bot,
                inputs=[message, image_upload, content_type_dropdown, chatbot],
                outputs=[chatbot, message]
            )
            clear_button.click(lambda: [], None, chatbot, queue=False)

        # Right Column: Tabs (Remains unchanged)
        with gr.Column(scale=1):
            with gr.Tabs():
                # ----- Tab 1: تصویر -----
                with gr.Tab("تصویر"):
                    prompt_box = gr.Textbox(label="پرامپت تصویر")
                    tool_dropdown = gr.Dropdown(
                        choices=['flux', 'midjourney', 'Dall-E'],
                        label="ابزار تولید تصویر"
                    )
                    generate_button = gr.Button("تولید تصویر")
                    output_image = gr.Image(label="خروجی تصویر")

                    generate_button.click(
                        generate_image,
                        inputs=[prompt_box, tool_dropdown],
                        outputs=output_image
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
                        choices=['runway', 'luma', 'pixverse'],
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
