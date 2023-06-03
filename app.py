import streamlit as st
from streamlit_card import card
#from streamlit.components.v1 import components

st.set_page_config(
    page_title="Cough severity Sclassification App",
    page_icon=":cough:",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

#some styles to remove padding and margins and menu
padding = 0
st.markdown(f""" <style>
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
    </style> """, unsafe_allow_html=True)

with st.sidebar:
    st.title("Navigation :")
    st.divider()
    choice = st.radio("Choose below to nagivate :",["Home", "About", "Contact","Github"])

if choice == "Home":
    col1, col2 = st.columns(2)
    #hero section
    with st.container():
        with col1:
            with st.container():
                st.title("Cough Classification")
                st.write("Cough classification using deep learning CNN involves training a convolutional neural network on cough audio samples to distinguish between different types of coughs. The network learns to extract relevant features from the audio signals, enabling accurate classification of coughs based on their characteristics.")
                cola, colb, colc, cold = st.columns(4)
                with cola:
                    a = st.button("Predict")
                    if a:
                        st.markdown(
                            '''
                               <h3>Write modal code here</h3> 
                            ''',
                            unsafe_allow_html=True
                        )
                with colb:
                    learn_more = st.button("Learn More")
                    if learn_more:
                        pass #will code the new page here
        with col2:
            with st.container():
                st.image(
                    'https://img.freepik.com/free-photo/young-man-suffering-from-cough-shirt-looking-ill_176474-20423.jpg?size=626&ext=jpg',caption="Coughing   ")

    #card section
    with st.container():
        col1, col2, col3 = st.columns(3)
    
        with col1:
            with st.container():
                Card1 = card(
                    text="Card 1",
                    title="Card 1",
                    image='https://img.freepik.com/free-vector/people-starting-business-project_23-2148866842.jpg?size=626&ext=jpg',
                    key="card1"
                )
            
        with col2:
                with st.container():
                    Card2 = card(
                        text="Card 1",
                        title="Card 1",
                        image='https://img.freepik.com/free-vector/people-starting-business-project_23-2148866842.jpg?size=626&ext=jpg',
                        key="card2"
                    )
 
        with col3:
                with st.container():
                    Card3 = card(
                        text="Card 1",
                        title="Card 1",
                        image='https://img.freepik.com/free-vector/people-starting-business-project_23-2148866842.jpg?size=626&ext=jpg'
                    )
        
if choice == "About":
        

    st.markdown('''
    <style>
    .about-section {
    padding: 50px 0;
    background-color: #000000;
    text-align: center;
    }

    .about-section h2 {
    margin-bottom: 30px;
    color: #ffffff;
    }

    .about-section p {
    font-size: 18px;
    line-height: 1.5;
    color: #ffffff;
    }

    .about-section .btn {
    margin-top: 20px;
    padding: 10px 20px;
    font-size: 16px;
    border-radius: 5px;
    background-color: #007bff;
    color: #ffffff;
    text-decoration: none;
    }

    .about-section .btn:hover {
    background-color: #0056b3;
    }
    </style>
    ''', unsafe_allow_html=True)

    st.markdown('''
    <section class="about-section">
    <div class="container">
        <h2>About the Project</h2>
        <p>This project is an ML-based application that aims to solve <strong>insert problem statement here</strong>. It utilizes state-of-the-art machine learning algorithms to achieve accurate predictions and provide valuable insights.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        <a class="btn" href="#">button</a>
    </div>
    </section>
    ''', unsafe_allow_html=True)

if choice == "Contact":
    st.write("# Contact Us")
    st.write("Please fill out the form below to get in touch with us.")
    
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    
    if st.button("Submit"):
        # You can add your code here to process the form submission, such as sending an email or storing the data in a database
        st.success("Thank you for reaching out. We will get back to you soon!")

if choice == ("Github"):

        st.markdown('''
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
        ''', unsafe_allow_html=True)

        st.title("Social Media Handles")

        # Add your social media logos and names here
        st.image('https://img.icons8.com/?size=512&id=pQiP0C7IB9GU&format=png', caption='Github', width=100, use_column_width=False)
        #st.image('path_to_logo2.png', caption='Logo 2', width=100, use_column_width=False)

        #st.image('path_to_logo3.png', caption='Logo 3', width=100, use_column_width=False)

