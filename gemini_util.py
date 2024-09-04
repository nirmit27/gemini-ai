import os

from PIL import Image
import google.generativeai as genai

# Loading the API key
genai.configure(api_key=os.environ.get("API_KEY"))


def load_gemini_pro(model_name: str) -> genai.GenerativeModel:
    """Returns the Gemini Pro Generative model."""
    model: genai.GenerativeModel = genai.GenerativeModel(model_name=model_name)
    return model


def img_caption(prompt: str, image: Image.Image) -> str:
    """Response for image captioning prompt."""
    model: genai.GenerativeModel = load_gemini_pro("gemini-1.5-flash")
    caption: str = model.generate_content([prompt, image]).text or ""
    return caption
