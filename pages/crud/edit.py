import streamlit as st
import controllers.clienteController as clienteController
import models.Clientes as clientes

listOccupation = ["Desenvolvedor", "Músico", "Designer", "Professor"]


'''
Todos os elementos do formulário estão em variáveis de 
sessão (veja mais aqui: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state)

Então coloquei uma key nos inputs pra poder pegar os valores deles depois com st.session_state.

Passei os valores pra sua função alterar e funcionou. Quer dizer, quase. Tinha um erro na query SQL.

'''


def click_handler():
    # Quando o botão for clicado eu pego 
    clienteController.alterar(clientes.Clientes(
    st.session_state.cliente_id, 
    st.session_state.new_name, 
    st.session_state.new_age,
    st.session_state.new_job))
    
    st.success("Cliente alterado com sucesso!")
 
def editarCliente(idAlteracao):
    
    cliente = clienteController.selecionar_id(idAlteracao)
    st.session_state.cliente_id = idAlteracao
    
    with st.form(key="update_client_form_" + str(idAlteracao)):
        
        st.text("Alterando cliente")
        name_input = st.text_input(label="Nome:", value=cliente.nome, key="new_name")
        
        idade_input = st.number_input(
            label="Idade", format="%d", step=1,
                value=cliente.idade, key="new_age")
        
        profissao_input = st.selectbox(
            "Selecione sua profissão", options=listOccupation,
            index=listOccupation.index(cliente.profissao), key="new_job")
        
        #on_click serve de callback, chama uma função quando o botão for clicado.
        st.form_submit_button(label="Alterar", on_click=click_handler)
        
     