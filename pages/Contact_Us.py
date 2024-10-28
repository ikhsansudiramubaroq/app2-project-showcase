import streamlit as st

st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Masukkan email anda")
    message = st.text_area("Pesan anda")
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        print("Ditekan")

