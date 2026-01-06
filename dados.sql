CREATE TABLE tbl_users(
    id_cliente SERIAL PRIMARY KEY,
	nome VARCHAR(65) NOT NULL,
	email VARCHAR(80) NOT NULL,
	senha VARCHAR(8) NOT NULL
)

SELECT * FROM tbl_users;

CREATE TABLE tbl_viagens(
	id_viagem SERIAL PRIMARY KEY,
	local_saida VARCHAR(95) NOT NULL,
	local_destinado VARCHAR(95) NOT NULL,
	data_saida DATE NOT NULL,
	valor INT NOT NULL
);
INSERT INTO tbl_users(nome, email, senha) VALUES
	('Jeremias','dossantosjeremias@gmail.com','12345678')
INSERT INTO tbl_viagens(local_saida, local_destinado, data_saida, valor) VALUES
	('Brasil','Mexico','2026-01-03',3000),
	('Brasil','Noruega','2026-01-01',4200),
	('Brasil','Mexico','2026-01-02',3000),
	('Brasil','Russia','2025-12-20',3500);
	
SELECT * FROM tbl_viagens

CREATE TABLE tbl_reservas (
    id_reserva SERIAL PRIMARY KEY,
    id_cliente INTEGER NOT NULL,
    id_viagem INTEGER NOT NULL,
    data_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'confirmada' CHECK (status IN ('pendente', 'confirmada', 'cancelada')),
	FOREIGN KEY (id_cliente) REFERENCES tbl_users(id_cliente)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_viagem) REFERENCES tbl_viagens(id_viagem)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    -- Garantir que um cliente não reserve a mesma viagem múltiplas vezes
    UNIQUE(id_cliente, id_viagem)
	);

CREATE INDEX idx_reservas_cliente ON tbl_reservas(id_cliente);
CREATE INDEX idx_reservas_viagem ON tbl_reservas(id_viagem);

INSERT INTO tbl_reservas (id_cliente, id_viagem, status) VALUES
    (1, 1, 'confirmada'),
    (1, 2, 'pendente');


