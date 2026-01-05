import os, psycopg as pg
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
address = os.getenv('DB_ADDRESS')
port = os.getenv('DB_PORT')
dbname = os.getenv('DB_NAME')

def get_connection():
    try:
        connection = pg.connect(f"user={user} password={password} host={address} port={port} dbname={dbname}")
        print('Banco de dados conectado com sucesso!')
        
        return connection
    except Exception as e:
        print(f"Erro: {e}")
        return None