import streamlit as st

st.markdown(
    """
    <style>
    body {
    background-color: black;
    color: white;
    font-family: Arial, sans-serif;
    padding: 20px;
    }

    h1 {
    text-align: center;
    margin-bottom: 20px;
    }

    .social-media-container {
    display: flex;
    justify-content: center;
    align-items: center;
    }

    .logo {
    margin: 20px;
    width: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Social Media Handles")

# Add your social media logos and names here
st.image(
    "https://img.icons8.com/?size=512&id=pQiP0C7IB9GU&format=png",
    caption="Github",
    width=100,
    use_column_width=False,
)
