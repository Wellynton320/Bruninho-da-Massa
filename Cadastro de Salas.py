import tkinter as tk
from tkinter import messagebox
import sqlite3

class SalaCadastroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Salas")

        self.root.geometry("300x250")

        self.conn = sqlite3.connect('salas.db')
        self.cursor = self.conn.cursor()
        self.criar_tabela()

        self.label_nome = tk.Label(root, text="Nome da Sala:")
        self.label_nome.pack(pady=5)
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack(pady=5)

        self.label_numero = tk.Label(root, text="Número da Sala:")
        self.label_numero.pack(pady=5)
        self.entry_numero = tk.Entry(root)
        self.entry_numero.pack(pady=5)

        self.label_predio = tk.Label(root, text="Prédio:")
        self.label_predio.pack(pady=5)
        self.entry_predio = tk.Entry(root)
        self.entry_predio.pack(pady=5)

        self.button_salvar = tk.Button(root, text="Salvar", command=self.salvar_sala)
        self.button_salvar.pack(pady=20)

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS salas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                numero TEXT NOT NULL,
                predio TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def salvar_sala(self):
        nome = self.entry_nome.get()
        numero = self.entry_numero.get()
        predio = self.entry_predio.get()

        if nome and numero and predio:
            self.cursor.execute('INSERT INTO salas (nome, numero, predio) VALUES (?, ?, ?)', (nome, numero, predio))
            self.conn.commit()
            messagebox.showinfo("Sucesso", f"Sala '{nome}' no prédio '{predio}' com número '{numero}' cadastrada com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = SalaCadastroApp(root)
    root.mainloop()