import streamlit as st
from streamlit_card import card

# from streamlit.components.v1 import components

st.set_page_config(
    page_title="Cough severity Sclassification App",
    page_icon=":cough:",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)

# some styles to remove padding and margins and menu
padding = 0
st.markdown(
    f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }}
    .css-14xtw13{{display:none;
    }}
    .stApp {{
        background: url("https://cutewallpaper.org/21/white-gradient-background-hd/Black-Gradient-Wallpaper-77+-images-.jpg");
        background-size: cover}}
    .css-1avcm0n{{display: none;}}
    .css-6qob1r{{background-color: #595959;}}
    </style> """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.title("Navigation :")
    st.divider()

col1, col2 = st.columns(2)
# hero section
with st.container():
    with col1:
        with st.container():
            st.title("Cough Classification")
            st.write(
                "Cough classification using deep learning CNN involves training a convolutional neural network on cough audio samples to distinguish between different types of coughs. The network learns to extract relevant features from the audio signals, enabling accurate classification of coughs based on their characteristics."
            )
            cola, colb, colc, cold = st.columns(4)
            with cola:
                a = st.button("Predict")
                if a:
                    st.markdown(
                        """
                            <h3>Write modal code here</h3>
                        """,
                        unsafe_allow_html=True,
                    )
            with colb:
                learn_more = st.button("Learn More")
                if learn_more:
                    pass  # will code the new page here
    with col2:
        with st.container():
            st.image(
                "https://img.freepik.com/free-photo/young-man-suffering-from-cough-shirt-looking-ill_176474-20423.jpg?size=626&ext=jpg",
                caption="Coughing   ",
            )

# card section
with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container():
            Card1 = card(
                text="Card 1",
                title="Card 1",
                image="https://img.freepik.com/free-vector/people-starting-business-project_23-2148866842.jpg?size=626&ext=jpg",
                key="card1",
            )

    with col2:
        with st.container():
            Card2 = card(
                text="Card 1",
                title="Card 1",
                image="https://img.freepik.com/free-vector/people-starting-business-project_23-2148866842.jpg?size=626&ext=jpg",
                key="card2",
            )

    with col3:
        with st.container():
            Card3 = card(
                text="Card 1",
                title="Card 1",
                image="https://img.freepik.com/free-vector/people-starting-business-project_23-2148866842.jpg?size=626&ext=jpg",
            )
