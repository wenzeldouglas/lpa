#Exemplo 07 - 8 de abril de 2024

nome = input("Digite o seu nome completo: ")
nascimento = input("Digite sua data de Nascimento <DD/MM/AAAA>: ")
data = nascimento.split('/')
palavra = nome.split()


pre_nome = palavra[0]
sobrenome = palavra [1]

print("========================================")
print(f'O Seu primeiro nome é: {pre_nome}')
print(f'O Seu sobrenome é: {sobrenome}')
print(f'Você nasceu no dia {data[0]} no mês {data[1]}')
print("========================================")