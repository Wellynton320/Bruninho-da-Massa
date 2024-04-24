import sqlite3

conn = sqlite3.connect('salas.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS Salas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    capacidade INTEGER NOT NULL,
    localizacao TEXT NOT NULL,
    equipamentos TEXT
);
''')

def cadastrar_sala(nome, capacidade, localizacao):
    conn.execute('''
    INSERT INTO Salas (nome, capacidade, localizacao)
    VALUES (?, ?, ?, ?)
    ''', (nome, capacidade, localizacao))
    conn.commit()

cadastrar_sala()

def listar_salas():
    cursor = conn.execute('SELECT * FROM Salas')
    for row in cursor:
        print("ID:", row[0])
        print("Nome:", row[1])
        print("Capacidade:", row[2])
        print("Localização:", row[3])
        print("Equipamentos:", row[4])
        print()

listar_salas()

conn.close()
