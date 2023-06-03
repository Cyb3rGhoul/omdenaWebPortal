import streamlit as st

st.write("# Contact Us")
st.write("Please fill out the form below to get in touch with us.")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Submit"):
    # TODO: code here to process the form submission, such as sending an email or storing the data in a database
    st.success("Thank you for reaching out. We will get back to you soon!")
