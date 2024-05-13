#Cadastro de Salas
import json

def cadastrar_sala():
    nome = input("Nome da sala: ")
    capacidade = input("Capacidade da sala: ")
    localizacao = input("Localização da sala: ")
    equipamentos = input("Equipamentos disponíveis (separados por vírgula): ").split(',')

    sala = {
        "nome": nome,
        "capacidade": capacidade,
        "localizacao": localizacao,
        "equipamentos": equipamentos
    }

    with open("salas.json", "a") as file:
        json.dump(sala, file)
        file.write('\n')
    
    print("Sala cadastrada com sucesso!")

def main():
    print("===== Cadastro de Salas =====")
    while True:
        opcao = input("1 - Cadastrar Sala\n0 - Sair\nEscolha uma opção: ")

        if opcao == '1':
            cadastrar_sala()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()