import streamlit as st
import controllers.clienteController as clienteController
import models.Clientes as clientes

listOccupation = ["Desenvolvedor", "Músico", "Designer", "Professor"]


class edit:
    _clienteController: clienteController.clienteController

    def __init__(self):
        self._clienteController = clienteController.clienteController()

    def click_handler(self):

        self._clienteController.alterar(clientes.Clientes(
            st.session_state.cliente_id,
            st.session_state.new_name,
            st.session_state.new_age,
            st.session_state.new_job))

        st.success("Cliente alterado com sucesso!")

    def editarCliente(self, idAlteracao):
        cliente = self._clienteController.selecionar_id(idAlteracao)
        st.session_state.cliente_id = idAlteracao

        with st.form(key="update_client_form_" + str(idAlteracao)):

            st.text("Alterando cliente")
            name_input = st.text_input(
                label="Nome:", value=cliente.nome, key="new_name")

            idade_input = st.number_input(
                label="Idade", format="%d", step=1,
                value=cliente.idade, key="new_age")

            profissao_input = st.selectbox(
                "Selecione sua profissão", options=listOccupation,
                index=listOccupation.index(cliente.profissao), key="new_job")

            st.form_submit_button(label="Alterar", on_click=self.click_handler)