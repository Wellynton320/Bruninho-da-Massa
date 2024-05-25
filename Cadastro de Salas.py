import json
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def validar_numeros(input):
    if input.isdigit() or input == "":
        return True
    else:
        return False

def cadastrar_sala():
    nome = nome_entry.get()
    capacidade = capacidade_entry.get()
    localizacao = localizacao_var.get()
    equipamentos = [equip.strip() for equip in equipamentos_entry.get().split(',')]

    sala = {
        "nome": nome,
        "capacidade": capacidade,
        "localizacao": localizacao,
        "equipamentos": equipamentos
    }

    with open("salas.json", "a") as file:
        json.dump(sala, file)
        file.write('\n')
    
    messagebox.showinfo("Sucesso", "Sala cadastrada com sucesso!")

def main():
    root = tk.Tk()
    root.title("Cadastro de Salas")
    root.geometry("1000x400")
    root.resizable(False, False)
    
    frame = ttk.Frame(root, padding="20 20 20 20")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    for i in range(4):
        frame.rowconfigure(i, weight=1)
        frame.columnconfigure(i, weight=1)

    ttk.Label(frame, text="Nome da sala:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
    ttk.Label(frame, text="Capacidade da sala:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    ttk.Label(frame, text="Localização da sala:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    ttk.Label(frame, text="Equipamentos disponíveis (separados por vírgula):").grid(row=3, column=0, sticky="e", padx=10, pady=5)

    global nome_entry, capacidade_entry, localizacao_var, equipamentos_entry
    nome_entry = ttk.Entry(frame, width=30)
    capacidade_entry = ttk.Entry(frame, width=30, validate="key")
    capacidade_entry['validatecommand'] = (capacidade_entry.register(validar_numeros), '%S')
    equipamentos_entry = ttk.Entry(frame, width=30)

    nome_entry.grid(row=0, column=1, padx=10, pady=5)
    capacidade_entry.grid(row=1, column=1, padx=10, pady=5)
    equipamentos_entry.grid(row=3, column=1, padx=10, pady=5)

    localizacao_var = tk.StringVar(root)
    localizacao_combobox = ttk.Combobox(frame, textvariable=localizacao_var, values=["Prédio Sede", "Prédio CTU"], state="readonly")
    localizacao_combobox.grid(row=2, column=1, padx=10, pady=5)
    localizacao_combobox.current(0)

    cadastrar_button = ttk.Button(frame, text="Cadastrar Sala", command=cadastrar_sala)
    cadastrar_button.grid(row=4, columnspan=2, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()