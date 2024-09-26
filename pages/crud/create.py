import streamlit as st
import controllers.clienteController as clienteController
import models.Clientes as clientes
import pages.crud.edit as editCliente


class create:
    _clienteController: clienteController.clienteController
    def __init__(self):
        self._clienteController = clienteController.clienteController()
    def cadastrar(self):
        idAlteracao = st.query_params
        idAlteracao = idAlteracao.get("id")
        if idAlteracao is None:
            st.write(idAlteracao)
            st.title("Tela de cadastro")
            with st.form(key="include_cliente"):
                input_name = st.text_input(label="Nome:")
                input_idade = st.number_input(label="Idade", format="%d", step=1)
                input_ocupation = st.selectbox(
                    "Selecione sua profissão", ["Desenvolvedor", "Músico",
                                                "Designer", "Professor"])
                button = st.form_submit_button("Enviar")

                if button:
                    if idAlteracao is None:
                        self._clienteController.incluir(clientes.Clientes(None, input_name, input_idade, input_ocupation))
                        st.success("Cliente incluído com sucesso!")

        else:
            editCliente.editarCliente()