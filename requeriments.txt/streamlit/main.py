import streamlit as st

st.title("Meu primeiro aplicativo")

nome = st.text_input("Qual é o seu nome?")

if st.button("Enviar"):
    st.success(f"Olá, {nome}!")