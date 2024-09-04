import os
from PIL import Image

import streamlit as st
from streamlit_option_menu import option_menu

from streamlit_util import (lb, page_header, translate_role)
from gemini_util import (load_gemini_pro, img_caption,
                         text_embedding, llm_response)


# Setting page configuration
work_dir: str = os.path.dirname(os.path.abspath(__file__))
st.set_page_config(
    page_title="Gemini AI",
    page_icon="💠",
    layout="centered"
)

# Options
selected: str = ""
options: list[str] = ["ChatBot", "Image captioning",
                      "Embed text", "Ask me anything"]
icons: list[str] = ["chat-dots-fill", "image-fill",
                    "textarea-t", "patch-question-fill"]


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
if selected == options[0]:
    gemini_response: str = ""
    model = load_gemini_pro("gemini-pro")

    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    page_header("✨ Gemini", color="lightblue")

    # Displaying the chat history so far ...
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role(message.role)):
            st.markdown(message.parts[0].text)

    user_prompt: str | None = st.chat_input("Ask Gemini Pro ...")
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        _, c2, _ = st.columns((3, 4, 1))

        with c2:
            with st.spinner('Generating response ...'):
                gemini_response = st.session_state.chat_session.send_message(
                    user_prompt).text

        with st.chat_message("assistant"):
            st.markdown(gemini_response)


# Image captioning page
if selected == options[1]:
    caption: str = ""
    page_header("📸 Snap Narrate", color="aqua")

    image_upload = st.file_uploader("Generate a descriptive caption for your image.", type=[
                                    ".jpg", ".jpeg", ".png"])

    if st.button("Generate Caption"):
        if image_upload:
            image: Image.Image = Image.open(image_upload)

            st.divider()
            col1, col2 = st.columns(2, gap="medium")

            with col1:
                image.thumbnail((600, 400))

                st.text("Image")
                st.image(image)

            with col2:
                with st.spinner('Generating response ...'):
                    caption = img_caption(image)

                st.text("Caption")
                st.info(caption)


# Text embedding page
if selected == options[2]:
    embeddings: list[float] = []
    page_header("🔡 Text Embedding", color="lightgreen")

    input_text: str = st.text_area(
        label="Enter the text to generate the embeddings.", placeholder="e.g. Who killed Hannibal?")

    if st.button("Get Embeddings"):
        _, col, _ = st.columns((2, 2, 2))

        with col:
            lb()
            with st.spinner('Generating embeddings ...'):
                embeddings = text_embedding(input_text)

        st.subheader("Embeddings", divider="green")
        st.markdown(f"""<code style="max-width: 20rem; color: white;">{
                    embeddings}</code>""", unsafe_allow_html=True)


# QnA page
if selected == options[-1]:
    result: str = ""
    page_header("❓ Ask Me Anything", color="slate")

    input_text: str = st.text_area(
        label="Enter your question.", placeholder="e.g. Can dogs look up?")

    if st.button("Ask Gemini"):
        _, col, _ = st.columns((2, 1, 2))

        with col:
            lb()
            with st.spinner("Thinking ..."):
                result = llm_response(input_text)

        st.subheader("Answer", divider="blue")
        st.markdown(result)
