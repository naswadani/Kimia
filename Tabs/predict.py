import streamlit as st
from web_function import predict

def app(df, x, y):
    st.title("Halaman Prediksi")

    col1, col2 = st.columns(2)
    with col1:
        Semester1 = st.text_input("Semester 1")
        Semester2 = st.text_input("Semester 2")
        Semester3 = st.text_input("Semester 3")
    with col2:
        Semester4 = st.text_input("Semester 4")
        Semester5 = st.text_input("Semester 5")

    features = [Semester1,Semester2,Semester3,Semester4,Semester5]
    
    # Tombol predict
    if st.button("Predict"):
        prediction, score = predict(x, y, features)
        score = score
        st.info("Predict Success")

        if (prediction == 0):
            st.warning("Mohon Maaf Anda Tidak Cocok Untuk Melanjutkan Kuliah Di Jurusan Kimia")
        else:
            st.success("Cocok Untuk Melanjutkan Kuliah Di Jurusan Kimia")

        st.write("Akurasi model adalah", (score * 100), "%")
    
    
