import streamlit as st

st.set_page_config(layout="wide")

# instance objek col1 dan col2
col1, col2 = st.columns(2)

# objek 1
with col1:
    st.image("images/photo.png")

# objek 2
with col2:
    st.title("Ikhsan Sudira Mubaroq")
    content = """
    Hi, Saya ikhsan sudira mubaroq dari Universitas Bina Sarana Informatika dan saya adalah programmer python
    saya bekerja di mana saja dan kapan saja,Hi, Saya ikhsan sudira mubaroq dari Universitas Bina Sarana Informatika dan saya adalah programmer python
    saya bekerja di mana saja dan kapan saja,Hi, Saya ikhsan sudira mubaroq dari Universitas Bina Sarana Informatika dan saya adalah programmer python
    saya bekerja di mana saja dan kapan saja,Hi, Saya ikhsan sudira mubaroq dari Universitas Bina Sarana Informatika dan saya adalah programmer python
    saya bekerja di mana saja dan kapan saja,Hi, Saya ikhsan sudira mubaroq dari Universitas Bina Sarana Informatika dan saya adalah programmer python
    saya bekerja di mana saja dan kapan saja,Hi, Saya ikhsan sudira mubaroq dari Universitas Bina Sarana Informatika dan saya adalah programmer python
    saya bekerja di mana saja dan kapan saja,Hi, Saya ikhsan sudira mubaroq dari Universitas Bina Sarana Informatika dan saya adalah programmer python
    saya bekerja di mana saja dan kapan saja,
    """
    st.info(content)

content2 = """
informasi lebih lanjut silahkan hubungi saya saja, saya akan melayani anda lebih lanjut !
"""
st.write(content2)