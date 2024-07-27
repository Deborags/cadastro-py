import streamlit as st
import controllers.clienteController as clienteController
import pages.crud.edit as editCliente
import pages.crud.create as createCliente


def listarClientes():
    paramsId = st.query_params
    if paramsId is not None:
        st.title("Clientes cadastrados")
        colms = st.columns((1, 2, 1, 2, 1, 1))
        campos = ["N°", "nome", "Idade", "Profissão", " ", " "]
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)

        for item in clienteController.selecionar_todos():
            col1, col2, col3, col4, col5, col6 = st.columns((1, 2, 1, 2, 1, 1))
            col1.write(item.id)
            col2.write(item.nome)
            col3.write(item.idade)
            col4.write(item.profissao)
            button_excluir = col5.empty()
            on_click_excluir = button_excluir.button(
                'Excluir', 'btnExcluir' + str(item.id))
            button_alterar = col6.empty()
            on_click_alterar = button_alterar.button(
                'Alterar', 'btnAlterar' + str(item.id))
            if on_click_excluir:
                clienteController.excluir(item.id)
                st.rerun()

            if on_click_alterar:
                st.query_params.id = [item.id]
                editCliente.alterar()
    else:
        createCliente.cadastrar()
