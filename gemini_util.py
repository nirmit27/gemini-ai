import os
import google.generativeai as genai

# Loading the API key
genai.configure(api_key=os.environ.get("API_KEY"))


def load_gemini_pro() -> genai.GenerativeModel:
    """Returns the Gemini Pro Generative model."""
    model: genai.GenerativeModel = genai.GenerativeModel("gemini-pro")
    return model
