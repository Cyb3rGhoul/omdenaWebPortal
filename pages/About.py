import streamlit as st

st.markdown(
    """
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
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
<section class="about-section">
<div class="container">
    <h2>About the Project</h2>
    <p>This project is an ML-based application that aims to solve <strong>insert problem statement here</strong>. It utilizes state-of-the-art machine learning algorithms to achieve accurate predictions and provide valuable insights.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
    <a class="btn" href="#">button</a>
</div>
</section>
""",
    unsafe_allow_html=True,
)
