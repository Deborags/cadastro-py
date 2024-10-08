import streamlit as st
import bancodedados.database as db
import models.Clientes as clientes


class clienteController:
    _db: db.database

    def __init__(self):
        self._db = db.database()

    def incluir(self, cliente):
        try:
            dados = [cliente.nome, cliente.idade, cliente.profissao]
            connect = self._db.get_connection()
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

    def selecionar_id(self, id):
        connect = self._db.get_connection()
        cursor = connect.cursor()
        cursor.execute("""SELECT * FROM clientes WHERE id = ?""", id)
        costumerList = []

        for row in cursor.fetchall():
            costumerList.append(clientes.Clientes(row[0], row[1], row[2], row[3]))
        cursor.close()
        return costumerList[0]


    def alterar(self, cliente):
        try:
            connect = self._db.get_connection()
            cursor = connect.cursor()
            cursor.execute("""UPDATE clientes
                        SET cliNome = ?,
                        cliIdade = ?,
                        cliProfissao = ?
                        WHERE id = ?
                        """, cliente.nome, cliente.idade, cliente.profissao, cliente.id)
            connect.commit()
            cursor.close()
        except Exception as e:
            print(f"erro ao alterar:{e}")

    def excluir(self, id):
        try:
            connect = self._db.get_connection()
            cursor = connect.cursor()
            cursor.execute("""
                DELETE FROM clientes WHERE id = ?""", id)
            connect.commit()
            cursor.close()
            print("Cliente excluído")
        except Exception as e:
            print(f"Erro ao excluír cliente: {e}")
        st.success("Cliente excluído!")

    def selecionar_todos(self):
        connect = self._db.get_connection()
        cursor = connect.cursor()
        cursor.execute("""SELECT * FROM clientes ORDER BY id ASC;""")
        costumerList = []

        for row in cursor.fetchall():
            costumerList.append(clientes.Clientes(row[0], row[1], row[2], row[3]))
        cursor.close()
        return costumerList