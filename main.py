import streamlit as st
import pages.crud.create as createCliente
import pages.crud.read as readCliente


class main:
    _readCliente: readCliente.read
    _createCliente: createCliente.create

def __init__(self):
    _readCliente = readCliente.read()
    _createCliente = createCliente.create()

    st.sidebar.title("Menu")
    page_cliente = st.sidebar.selectbox("Escolha uma opção abaixo:", [
        "Home", "Incluir", "Consultar"])

    if page_cliente == "Home":
        st.title("Bem vindo")
        st.text("Olá, tudo bem? \n Selecione alguma opção no menu ao lado para"
                "interagir com o nosso projeto")

    if page_cliente == "Incluir":
        st.query_params.clear()
        _createCliente.cadastrar()

    if page_cliente == "Consultar":
        _readCliente.listarClientes()