import os
from streamlit import secrets

from PIL import Image
import google.generativeai as genai

API_KEY = secrets["API_KEY"]
genai.configure(api_key=API_KEY)


def load_gemini_pro(model_name: str) -> genai.GenerativeModel:
    """Returns the Gemini Pro Generative model."""
    model: genai.GenerativeModel = genai.GenerativeModel(model_name=model_name)
    return model


def img_caption(image: Image.Image) -> str:
    """Returns the response for image captioning prompt."""
    model: genai.GenerativeModel = load_gemini_pro("gemini-1.5-flash")
    caption: str = model.generate_content(
        ["Write a short caption for this image.", image]).text or ""
    return caption


def text_embedding(input_text: str) -> list[float]:
    """Returns the response containing text embeddings for the given input."""
    embedding_model: str = "models/embedding-001"
    embedding: dict = genai.embed_content(model=embedding_model,
                                          content=input_text,
                                          task_type="retrieval_document")
    return embedding["embedding"]


def llm_response(user_prompt: str) -> str:
    """Returns the response from the Gemini Pro LLM for a given user prompt."""
    llm_model: genai.GenerativeModel = load_gemini_pro("gemini-pro")
    result: str = llm_model.generate_content(user_prompt).text
    return result
