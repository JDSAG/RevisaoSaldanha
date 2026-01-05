from database.connection import * 
from database.queries import * 

def buy_trip (id_cliente,id_viagem,status):
    with get_connection() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try: 
                    cur.execute(BUY_TRIP,(id_cliente,id_viagem,status))
                    print(f'Viagem comprada com sucesso!') 
                except Exception as e:
                    print(e)
                    return None
    return None

def check_trip():
    with get_connection() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try: 
                    cur.execute(CHECK_TRIPS)
                    return cur.fetchall()
                except Exception as e:
                    print(e)
                    return None
    return None 

def update_date_trip():
    with get_connection() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try: 
                    cur.execute()
                except Exception as e:
                    print(e)
                    return None
    return None 