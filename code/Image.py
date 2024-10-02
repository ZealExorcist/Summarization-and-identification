import base64
import io
import gradio as gr
from groq import Groq
from PIL import Image
import requests

def encode_image(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def analyze_image(image, prompt, is_url=False):
    client = Groq()

    if is_url:
        image_content = {"type": "image_url", "image_url": {"url": image}}
    else:
        base64_image = encode_image(image)
        image_content = {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        image_content,
                    ],
                }
            ],
            model="llava-v1.5-7b-4096-preview",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def check_content_safety(image_description):
    client = Groq()

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a content safety classifier. Analyze the given text and determine if it contains any unsafe or inappropriate content."},
                {"role": "user", "content": f"Please analyze this image description for any unsafe or inappropriate content: {image_description}"}
            ],
            model="llama-guard-3-8b",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
def process_image(image, url, prompt):
    if image is not None:
        return analyze_image(image, prompt), check_content_safety(analyze_image(image, prompt))
    elif url:
        try:
            response = requests.get(url)
            image = Image.open(io.BytesIO(response.content))
            return analyze_image(url, prompt, is_url=True), check_content_safety(analyze_image(url, prompt, is_url=True))
        except:
            return "Invalid image URL. Please provide a direct link to an image.", ""
    else:
        return "Please provide an image to analyze.", ""
    
def launch():
    with gr.Blocks(
        theme=gr.themes.Soft(primary_hue="emerald",secondary_hue="amber"),
        css="""
        #app-container { max-width: 1000px; margin: auto; padding: 10px; }
        #title { text-align: center; margin-bottom: 10px; font-size: 24px; }
        #groq-badge { text-align: center; margin-top: 10px; }
        .gr-button { border-radius: 15px; }
        .gr-input, .gr-box { border-radius: 10px; }
        .gr-form { gap: 5px; }
        .gr-block.gr-box { padding: 10px; }
        .gr-paddle { height: auto; }
        """
    ) as demo:
        with gr.Column(elem_id="app-container"):
            gr.Markdown("# Image Summariser and Safety checker", elem_id="title")
            
            with gr.Row():
                prompt = gr.Textbox(
                    label="Image Analysis Prompt:",
                    value="Describe the image content.",
                    scale=3
                )
            
            with gr.Row():
                with gr.Column(scale=1):
                    image_input = gr.Image(type="pil", label="Upload Image:", height=200, sources=["upload"])
                with gr.Column(scale=1):
                    url_input = gr.Textbox(label="Or Paste Image URL:", lines=1)
                    analyze_button = gr.Button("🚀 Analyze Image", variant="primary")
            
            with gr.Row():
                with gr.Column():
                    analysis_output = gr.Textbox(label="Image Analysis with LlaVA 1.5 7B:", lines=6)
                with gr.Column():
                    safety_output = gr.Textbox(label="Safety Check with Llama Guard 3 8B:", lines=6)
            
            analyze_button.click(
                fn=process_image,
                inputs=[image_input, url_input, prompt, ],
                outputs=[analysis_output, safety_output]
            )
            
            with gr.Row():
                    
                with gr.Column():
                    gr.Markdown("""
                    **How to use this app:** 
                    1. Upload an image file or paste an image URL.
                    2. Use default prompt or enter custom prompt for image analysis.
                    3. Click "Analyze Image" to check for content safety.
                    """)
    
    demo.launch()

if __name__ == "__main__":
    launch()