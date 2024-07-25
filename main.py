import streamlit as st
import pages.crud.create as createcliente
import pages.crud.read as readCliente

st.sidebar.title("Menu")
page_cliente = st.sidebar.selectbox("Escolha uma opção abaixo:", [
    "Home", "Incluir", "Consultar"])

if page_cliente == "Home":
    st.title("Bem vindo")
    st.text("Olá, tudo bem? \n Selecione alguma opção no menu ao lado para"
            "interagir com o nosso projeto")

if page_cliente == "Incluir":
    createcliente.cadastrar()

if page_cliente == "Consultar":
    readCliente.listarClientes()
