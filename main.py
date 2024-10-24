import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ikhsan Sudira Mubaroq")
    content = """
    Hi, Saya ikhsan sudira mubaroq dari Universitas Bina Sarana Informatika dan saya adalah programmer python
    saya bekerja di mana saja dan kapan saja, tes
    """
    st.info(content)