import pyodbc

SERVER = 'DESKTOP-CT7COQP\\MNDEBORA'
DATABASE = 'cadastro'
USERNAME = 'sa'
PASSWORD = 'Debora20*'

connectionString = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={SERVER};'
    f'DATABASE={DATABASE};'
    f'UID={USERNAME};'
    f'PWD={PASSWORD};'
)

try:
    connect = pyodbc.connect(connectionString)
    print("Conexão estabelecida com sucesso")
except Exception as e:
    print(f'Erro ao conectar ao banco de dados: {e}')


def get_connection():
    return connect
