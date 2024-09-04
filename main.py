import os
from PIL import Image

import streamlit as st
from streamlit_option_menu import option_menu

from gemini_util import (load_gemini_pro, img_caption)

work_dir: str = os.path.dirname(os.path.abspath(__file__))


def translate_role(user_role: str) -> str:
    """Translates the role for the Streamlit app."""
    return "assistant" if user_role == "model" else user_role


# Setting page configuration
st.set_page_config(
    page_title="Gemini AI",
    page_icon="💠",
    layout="centered"
)

# Options
selected: str
options: list[str] = ["ChatBot", "Image captioning",
                      "Embed text", "Ask me anything"]
icons: list[str] = ["chat-dots-fill", "image-fill",
                    "textarea-t", "patch-question-fill"]

# Page layout -


def lb(n: int = 1) -> None:
    """For generating line breaks."""
    for _ in range(n):
        st.markdown('''
        <br>
        ''', unsafe_allow_html=True)


# Options sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Gemini AI",
        options=options,
        menu_icon="robot",
        icons=icons,
        default_index=0
    )


# ChatBot page
if selected == "ChatBot":
    # Loading the Gemini Pro Generative model
    model = load_gemini_pro("gemini-pro")

    # Initialising chat session in Streamlit if not already active
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    st.title("🤖 ChatBot")

    # Displaying the chat history so far ...
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role(message.role)):
            st.markdown(message.parts[0].text)

    # Input field for ChatBot
    user_prompt: str | None = st.chat_input("Ask Gemini Pro ...")
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        # Displaying the response from Gemini
        gemini_response: str = st.session_state.chat_session.send_message(
            user_prompt).text
        with st.chat_message("assistant"):
            st.markdown(gemini_response)


# Image captioning page
if selected == "Image captioning":
    st.title("📸 Snap Narrate")

    # Input image
    image_upload = st.file_uploader("Generate a descriptive caption for your image.", type=[
                                    ".jpg", ".jpeg", ".png"])

    if st.button("Generate Caption"):
        if image_upload:
            image: Image.Image = Image.open(image_upload)

            col1, col2 = st.columns(2, gap="medium")

            with col1:
                image.thumbnail((800, 600))
                lb(1)
                st.image(image)

            default_prompt: str = "Write a short caption for this image."

            # Fetching the response from Gemini Flash model
            caption: str = img_caption(default_prompt, image)

            with col2:
                lb(1)
                st.info(caption)
