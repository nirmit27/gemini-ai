import streamlit as st


def lb(n: int = 1) -> None:
    """For generating line breaks."""
    for _ in range(n):
        st.markdown('''
        <br>
        ''', unsafe_allow_html=True)


def page_header(title: str, color: str, size: float = 2.6, top: int = 30, bottom: int = 20) -> None:
    """For custom page headers/titles."""
    st.markdown(f"""
    <h1 style="text-align: center; color: {color}; font-size: {size}rem; margin-top: -{top}px;  margin-bottom: {bottom}px">
    {title}
    </h1>
    """, unsafe_allow_html=True)


def translate_role(user_role: str) -> str:
    """Translates the role for the Streamlit app."""
    return "assistant" if user_role == "model" else user_role
