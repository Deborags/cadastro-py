import streamlit as st
import controllers.clienteController as clienteController
import models.clientes as clientes


def editarCliente():
    idAlteracao = st.query_params
    idAlteracao = idAlteracao.get("id")
    global clienteRecuperado
    clienteRecuperado = None
    clienteRecuperado = clienteController.selecionar_id(idAlteracao)
    if clienteRecuperado is not None:
        st.query_params.id = [clienteRecuperado.id]
        # st.query_params.clear()
        with st.form(key="alterar_cliente"):
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
            # input_button_submit = st.form_submit_button(
            #     label="Alterar", on_click=jose())

            def jose():
                clienteController.alterar(clientes.Clientes(
                    clienteRecuperado, input_name, input_idade,
                    input_ocupation))
                st.success("Cliente alterado com sucesso!")
                print("fora", clienteRecuperado)
            print("qualquer coisa")
            input_button_submit = st.form_submit_button(
                label="Alterar", on_click=jose())