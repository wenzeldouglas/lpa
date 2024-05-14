#Faça um algoritmo que solicite uma data no formato de uma string – dd/mm/aaaa.
# Mostre essa data no formato AAAAMMDD

nasc = input("Digite sua data de nascimento <DD/MM/AAAA>: ")
data = nasc.split('/')
new = data[2] + data[1] + data[0]

print(new)

print("==============================")
print(f'Você nasceu no dia {data[0]}')
print(f'Você nasceu no mês {data[1]}')
print(f'Você nasceu no ano {data[2]}')
print(f'Chave para o banco de dados: {new}')
print("==============================")