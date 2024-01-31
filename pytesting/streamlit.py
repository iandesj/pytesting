import streamlit as st


def write_h1(text: str):
    st.markdown(f"# {text}")


def write_h2(text: str):
    st.markdown(f"## {text}")


def write_h3(text: str):
    st.markdown(f"### {text}")


def write_paragraph(text: str):
    st.markdown(text)


def bordered_image(image_path: str, caption: str):
    image_container = st.container(border=True)
    image_container.image(image_path, caption=caption)
