from datetime import datetime

def valida_data(ano="",mes="",dia=""):
    if(dia <= 31 and mes <= 12):
        hoje = datetime.now().date()
        data_nasc = datetime(ano, mes, dia).date()
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        if(idade >= 18):
            return True
        else:
            return False
    else:
        return False
def exibir_menu():
    print('Tecle:')
    print('1 - Cadastrar')
    print('2 - Exibir Mensagem')
    print('3 - Sair')
def cadastrar():
    nome = input("Digite o seu primeiro nome: ")
    sobrneome = input("Digite o seu sobrenome: ")
    cpf = input("Digite o seu CPF: ")
    #if not valida_cpf(cpf):
        #print("CPF Inválido!")
        #return
    data = input("Digite sua data de nascimento (DD/MM/AAAA)")
    if len(data) == 8:
        d = int(data[0:2])
        m = int(data[3:5])
        a = int(data[4:8])
    if len(data) == 10:
        data = data.split("/")
    if (len(data) == 3):
        a = int(data[2])
        m = int(data[1])
        d = int(data[0])
    else:
        print("Digite uma data válida")

    if not valida_data(a, m, d):
        print("Utilize o formato DD/MM/AAAA) ")
    renda_bruta = float(input("Digite sua renda bruta: "))
def exibir_mensagem():
        1 = ("A persistência realiza o impossível")
        2 = ("Seus sonhos não precisam de plateia, eles só precisam de você")
        3 = ("A persistência é o caminho do êxito")
        4 = ("No meio da dificuldade encontra-se a oportunidade")
def main():
    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            exibir_mensagem()
        elif opcao == 3:
            print("Bye Bye!")
            break
        else:
            print("Opção inválida!")


main()
