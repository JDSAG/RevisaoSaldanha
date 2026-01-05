from database.connection import * 
from database.queries import * 

def insert_client(nome:str,email:str, senha:str):
    with get_connection() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:                   
                    #Executar a consulta SQL
                    cur.execute(INSERT_USER, (nome,email, senha))
                    print(f'Cliente {nome} cadastrado com sucesso!')
                except Exception as e:
                    print(f'Error: {e}')
                    return None
                
        return None 
    
def login(nome:str,email:str, senha:str):
    with get_connection() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try: 
                    cur.execute(CHECK_USER, (nome, email, senha))
                    user = cur.fetchone()
                    if user is not None:
                        if user[3] == senha:
                            print(f"Sucesso no login! Bem-vindo, {nome}")
                            return user
                    else:
                        print("Usuário não encontrado")
                        return None

                except Exception as e:
                    print(f"Erro no login: {e}")
                    return None
    return None
