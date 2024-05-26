DROP TABLE IF EXISTS Reservas;
DROP TABLE IF EXISTS Login;
DROP TABLE IF EXISTS Laboratorios;
DROP TABLE IF EXISTS Usuarios;

-- Tabela de Login
CREATE TABLE IF NOT EXISTS Login (
    id_login INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome_usuario VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

-- Tabela de Laboratorios
CREATE TABLE IF NOT EXISTS Laboratorios (
    id_laboratorio INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(255),
    telefone VARCHAR(20)
);

-- Tabela de Cadastro de Usuários
CREATE TABLE IF NOT EXISTS Usuarios (
    id_usuario INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);

-- Tabela de Reservas de Laboratórios
CREATE TABLE IF NOT EXISTS Reservas (
    id_reserva INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT UNSIGNED,
    id_laboratorio INT UNSIGNED,
    data_reserva DATE,
    hora_inicio TIME,
    hora_fim TIME,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_laboratorio) REFERENCES Laboratorios(id_laboratorio)
);