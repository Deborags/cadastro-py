import streamlit as st
import services.database as db
import models.Clientes as Clientes


def incluir(cliente):
    try:
        dados = (cliente.nome, cliente.idade, cliente.profissao)
        connect = db.get_connection()
        cursor = connect.cursor()
        cursor.execute("""
            INSERT INTO clientes (
                cliNome,
                cliIdade,
                cliProfissao
            )
            VALUES (?, ?, ?)""", dados)
        connect.commit()
        cursor.close()
        print("Cliente incluído!")
    except Exception as e:
        print(f"Erro ao incluir cliente: {e}")


def excluir(id):
    try:
        connect = db.get_connection()
        cursor = connect.cursor()
        cursor.execute("""
            DELETE FROM clientes WHERE id = ?""", id)
        connect.commit()
        cursor.close()
        print("Cliente excluído")
    except Exception as e:
        print(f"Erro ao excluír cliente: {e}")
    st.success("Cliente excluído!")


def selecionar_todos():
    connect = db.get_connection()
    cursor = connect.cursor()
    cursor.execute("""SELECT * FROM clientes""")
    costumerList = []

    for row in cursor.fetchall():
        costumerList.append(Clientes.Clientes(row[0], row[1], row[2], row[3]))
    cursor.close()
    return costumerList
