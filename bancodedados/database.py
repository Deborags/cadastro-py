"""
Connects to a SQL database using pyodbc
"""
import pyodbc


class database:
    SERVER = 'DESKTOP-CT7COQP\\MNDEBORA'
    DATABASE = 'cadastro'
    USERNAME = 'sa'
    PASSWORD = 'Debora20*'
    connect: pyodbc.Connection = None

    connectionString = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={SERVER};'
        f'DATABASE={DATABASE};'
        f'UID={USERNAME};'
        f'PWD={PASSWORD};'
    )

    def __init__(self):
        try:
            self.connect = pyodbc.connect(self.connectionString)
            print("Conexão estabelecida com sucesso")
        except Exception as e:
            print(f'Erro ao conectar ao banco de dados: {e}')

    def get_connection(self) -> pyodbc.Connection:
        return self.connect