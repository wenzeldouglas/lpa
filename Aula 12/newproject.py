import random
import datetime

def exibir_menu():
    print("Menu:")
    print("1 - Cadastrar")
    print("2 - Exibir Mensagem")
    print("3 - Sair")

def cadastrar():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    cpf = input("Digite o CPF: ")
    if not cpf_validator.validate(cpf):
        print("CPF inválido.")
        return
    data_nascimento = input("Digite a data de nascimento (formato: dd/mm/aaaa): ")
    try:
        data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y").date()
    except ValueError:
        print("Data de nascimento inválida.")
        return
    renda_bruta = float(input("Digite a renda bruta: "))
    # Aqui você pode fazer o que quiser com os dados, como salvar em um banco de dados, por exemplo.

def exibir_mensagem():
    mensagens = [
        "A persistência realiza o impossível",
        "Seus sonhos não precisam de plateia, eles só precisam de você",
        "A persistência é o caminho do êxito",
        "No meio da dificuldade encontra-se a oportunidade"
    ]
    mensagem_aleatoria = random.choice(mensagens)
    print(mensagem_aleatoria)

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            exibir_mensagem()
        elif opcao == '3':
            print("Bye bye!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()