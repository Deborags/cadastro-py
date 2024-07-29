import streamlit as st
import controllers.clienteController as clienteController
import models.clientes as clientes


class edit:
    _clienteController: clienteController.clienteController

    def __init__(self):
        self._clienteController = clienteController.clienteController()

    def editarCliente(self):
        idAlteracao = st.query_params
        idAlteracao = idAlteracao.get("id")
        clienteRecuperado = None
        clienteRecuperado = self._clienteController.selecionar_id(idAlteracao)

        if clienteRecuperado is not None:
            st.query_params.id = [clienteRecuperado.id]
            st.query_params.clear()
            with st.form(key="include_cliente"):
                listOccupation = ["Desenvolvedor", "Músico",
                                  "Designer", "Professor"]
                st.text("Alterando cliente")
                input_name = st.text_input(
                    label="Nome:", value=clienteRecuperado.nome)
                input_idade = st.number_input(label="Idade", format="%d", step=1,
                                              value=clienteRecuperado.idade)
                input_ocupation = st.selectbox(
                    "Selecione sua profissão", options=listOccupation,
                    index=listOccupation.index
                    (clienteRecuperado.profissao))
                submit = st.form_submit_button(label="Atualizar")
                print("dentro do button")
                print(submit)
                if submit:
                    print("dentro do button")
                    # if idAlteracao is None:
                    self._clienteController.alterar(clientes.Clientes(
                        clienteRecuperado, input_name, input_idade,
                        input_ocupation))
                    st.success("Cliente alterado com sucesso!")
