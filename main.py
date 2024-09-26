import streamlit as st
import pages.crud.create as createCliente
import pages.crud.read as readCliente


class main:
    _readCliente: readCliente.read
    _createCliente: createCliente.create

    def __init__(self):
        self._readCliente = readCliente.read()
        self._createCliente = createCliente.create()
    
    def render(self):
        st.sidebar.title("Menu")
        page_cliente = st.sidebar.selectbox("Escolha uma opção abaixo:", [
            "Home", "Incluir", "Consultar"])

        if page_cliente == "Home":
            st.title("Bem-vindo")
            st.text("Olá, tudo bem? \nSelecione alguma opção no menu ao lado para"
                    " interagir com o nosso projeto")

        elif page_cliente == "Incluir":
            self._createCliente.cadastrar()

        elif page_cliente == "Consultar":
            self._readCliente.listarClientes()


if 'main_instance' not in st.session_state:
    st.session_state.main_instance = main()

st.session_state.main_instance.render()