CREATE DATABASE bandejao
USE bandejao;

CREATE TABLE usuario (
    id SERIAL NOT NULL,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    tipo SMALLINT NOT NULL,
    vinculo_escolar VARCHAR(255) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE categoria (
    id SERIAL NOT NULL,
    nome VARCHAR(100) NOT NULL,
    PRiMARY KEY(id)
);

CREATE TABLE fila (
    id SERIAL NOT NULL,
    categoria_id INT NOT NULL,
    nome_fila VARCHAR(100) NOT NULL,
    data_hora TIMESTAMP NOT NULL,
    quantidade INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(categoria_id) REFERENCES categoria(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE reserva (
    usuario_id INT NOT NULL,
    fila_id INT NOT NULL,
    posicao INT NOT NULL,
    PRIMARY KEY(usuario_id, fila_id),
    FOREIGN KEY(usuario_id) REFERENCES usuario(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(fila_id) REFERENCES fila(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE administrador (
    id SERIAL NOT NULL,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    vinculo_escolar VARCHAR(255) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE cardapio (
    id SERIAL NOT NULL,
    link VARCHAR(255) NOT NULL,
    PRIMARY KEY(id)
);