-- Tabela de Login
CREATE TABLE Login (
    id_login SERIAL PRIMARY KEY,
    nome_usuario VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

-- Tabela de Laboratorios
CREATE TABLE Laboratorios (
    id_laboratorio SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    localização VARCHAR(255)
);

-- Tabela de Cadastro de Usuários
CREATE TABLE Usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);

-- Tabela de Reservas de Laboratórios
CREATE TABLE Reservas (
    id_reserva SERIAL PRIMARY KEY,
    id_usuario INT,
    id_laboratorio INT,
    data_reserva DATE,
    hora_inicio TIME,
    hora_fim TIME,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_laboratorio) REFERENCES Laboratorios(id_laboratorio)
);
