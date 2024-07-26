import streamlit as st
import controllers.clienteController as clienteController
import models.Clientes as Clientes


def cadastrar():
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
            input_button_submit = st.form_submit_button("Enviar")

            if input_button_submit:
                clienteController.incluir(Clientes.Clientes(
                    None, input_name, input_idade, input_ocupation))
                st.success("Cliente incluído com sucesso!")

    else:
        idAlteracao = st.query_params
        idAlteracao = idAlteracao.get("id")
        st.write(idAlteracao)
        st.title("Alterar cliente")
        with st.form(key="include_cliente"):
            input_name = st.text_input(label="Nome:")
            input_idade = st.number_input(label="Idade", format="%d", step=1)
            input_ocupation = st.selectbox(
                "Selecione sua profissão", ["Desenvolvedor", "Músico",
                                            "Designer", "Professor"])
            input_button_submit = st.form_submit_button("Enviar")

            if input_button_submit:
                clienteController.incluir(Clientes.Clientes(
                    None, input_name, input_idade, input_ocupation))
                st.success("Cliente incluído com sucesso!")
