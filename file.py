import streamlit as st
import time

def rumuscc(l,p):
    cc = 0.785 * p * p * l
    return cc  


def main():
    st.title("Menghitung CC Kendaraan")
    foto = "foto2.jpg"
    
    st.image(foto)


    langkah = st.number_input("Masukkan langkah kendaraan\t: ")
    piston = st.number_input("Masukkan piston kendaraan\t: ")
    tombol = st.button("hitung")
    if tombol:
        hasil = rumuscc(langkah,piston)

        col1, col2, col3 = st.columns([langkah,piston, hasil])

        with col1:
            st.header("Langkah Kendaraan")
            st.write(langkah)
            
        with col2:
            st.header("Piston Kendaraan")
            st.write(piston)
        
        with col3:
            st.header("Total CC")
            st.write(hasil)


if __name__ == "__main__":
    main()
