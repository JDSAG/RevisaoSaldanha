from database.connection import * 
from database.queries import * 
from validations import validations as v
def buy_trip (id_cliente:int,id_viagem:int,status:str):
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
                    cur.execute(CHECK_USER_TRIPS)
                    return cur.fetchall()
                except Exception as e:
                    print(e)
                    return None
    return None 

def check_all_trips():
    with get_connection() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try: 
                    cur.execute(CHECK_ALL_TRIPS)
                    return cur.fetchall()
                except Exception as e:
                    print(e)
                    return None
    return None 

def cancel_trip(id_reserva:int):
    with get_connection() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(CANCEL_TRIP,(id_reserva,))
                    print(f"Viagem cancelada com sucesso") 
                except Exception as e:
                    print(e)
                    return None
    return None 

def update_date_trip(novo_id_viagem:int, id_cliente:int,viagem_atual_id: int):
    with get_connection() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                    try: 
                        cur.execute(UPDATE_DATE_TRIP,(novo_id_viagem, id_cliente, viagem_atual_id))
                        CONN.commit()
                        print("Viagem atualizada com sucesso") 
                    except Exception as e:
                        print(e)
                        return None
                    return None
    return None 