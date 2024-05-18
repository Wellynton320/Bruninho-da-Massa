import json
import tkinter as tk
from tkinter import messagebox

def validar_numeros(input):
    if input.isdigit() or input == "":
        return True
    else:
        return False

def cadastrar_sala():
    nome = nome_entry.get()
    capacidade = capacidade_entry.get()
    localizacao = localizacao_var.get()
    equipamentos = equipamentos_entry.get().split(',')

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

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    tk.Label(frame, text="Nome da sala:").grid(row=0, column=0, sticky="e")
    tk.Label(frame, text="Capacidade da sala:").grid(row=1, column=0, sticky="e")
    tk.Label(frame, text="Localização da sala:").grid(row=2, column=0, sticky="e")
    tk.Label(frame, text="Equipamentos disponíveis (separados por vírgula):").grid(row=3, column=0, sticky="e")

    global nome_entry, capacidade_entry, localizacao_var, equipamentos_entry
    nome_entry = tk.Entry(frame)
    capacidade_entry = tk.Entry(frame, validate="key")
    capacidade_entry['validatecommand'] = (capacidade_entry.register(validar_numeros), '%S')
    equipamentos_entry = tk.Entry(frame)
    
    localizacao_var = tk.StringVar(root)
    localizacao_combobox = tk.OptionMenu(frame, localizacao_var, "Prédio Sede", "Prédio CTU")
    localizacao_combobox.grid(row=2, column=1, sticky="w")

    nome_entry.grid(row=0, column=1)
    capacidade_entry.grid(row=1, column=1)
    equipamentos_entry.grid(row=3, column=1)

    cadastrar_button = tk.Button(frame, text="Cadastrar Sala", command=cadastrar_sala)
    cadastrar_button.grid(row=4, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()