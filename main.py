import streamlit as st
import pandas

st.set_page_config(layout="wide")

# membagi 2 columns yaitu col1 dan col2
col1, col2 = st.columns(2)

# objek 1
with col1:
    st.image("images/photo.png")

# objek 2
with col2:
    # membuat title
    st.title("Ikhsan Sudira Mubaroq")
    # membuat content
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

# membagi 3 bagian kolom secara horizontal
col3, kolom_kosong,col4 = st.columns([1.5, 0.5, 1.5])

# fungsi pandas membaca file csv dan menggunakan fungsi 'separator' yaitu pemisah antar kolom
df = pandas.read_csv("data.csv", sep=";")

with col3:
    # pengulanan for dari 0-10 baris dan diulangi menggunakan header
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        # images yaitu folder
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    # pengulanan for dari 10-11 baris dan diulangi menggunakan header
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        # images yaitu folder
        st.image("images/" + row["image"])
        # perbedaan source code jika tidak ditambah []
        st.write(f"Source Code ({row['url']})")


