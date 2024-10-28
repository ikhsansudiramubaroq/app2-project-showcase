import streamlit as st
from pengirim_email import send_email

# Menampilkan header di aplikasi Streamlit
st.header("Contact Us")

# Membuat form menggunakan Streamlit
with st.form(key="email_forms"):
    # Input untuk pengguna memasukkan alamat email mereka
    user_email = st.text_input("Masukkan email anda")
    # Input area teks untuk pengguna menuliskan pesan mereka
    raw_message = st.text_area("Pesan anda")

    # Membuat format pesan yang akan dikirim melalui email
    message = f"""\ 
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    # Tombol untuk submit form
    button = st.form_submit_button("Submit")
    # Menampilkan nilai tombol submit (True jika diklik, False jika belum)
    print(button)

    # Jika tombol submit diklik, maka akan mengirim email
    if button:
        # Memanggil fungsi send_email untuk mengirimkan pesan yang sudah diformat
        send_email(message)
        # Menampilkan informasi bahwa pesan berhasil dikirim
        st.info("Pesan anda berhasil dikirim")
