INSERT_USER = '''INSERT INTO tbl_users(nome, email, senha)
                    VALUES (%s, %s, %s);'''
                    
CHECK_USER = '''SELECT * FROM tbl_users WHERE nome = %s AND email = %s AND senha = %s'''

BUY_TRIP = '''INSERT INTO tbl_reservas(id_cliente,id_viagem,status) VALUES (%s,%s,%s)'''

CHECK_USER_TRIPS = '''SELECT 
    r.id_reserva,
    r.data_reserva,
    r.status,
    u.id_cliente,
    u.nome,
    u.email,
    v.id_viagem,
    v.local_saida,
    v.local_destinado,
    v.data_saida,
    v.valor
FROM tbl_reservas r
INNER JOIN tbl_users u ON r.id_cliente = u.id_cliente
INNER JOIN tbl_viagens v ON r.id_viagem = v.id_viagem;'''

CANCEL_TRIP = '''DELETE FROM tbl_reservas WHERE id_reserva = %s'''

UPDATE_DATE_TRIP = '''UPDATE tbl_reservas SET id_viagem =%s WHERE id_cliente = %s AND id_viagem = %s'''

CHECK_ALL_TRIPS = '''SELECT * FROM tbl_viagens'''

SEARCH_ID_TRIP = '''SELECT id_viagem FROM tbl_viagens WHERE id_viagem = %s'''