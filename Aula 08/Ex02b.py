data = input("Digite a data de nascimento <DD/MM/AAAA>: ")
dia = data[0:2]
mes = data[3:5]
ano = data[6::]
data_invertida = ano+mes+dia

print(data_invertida)

print("==============================")
print(f'Você nasceu no dia {dia}')
print(f'Você nasceu no mês {mes}')
print(f'Você nasceu no ano {ano}')
print(f'Chave para o banco de dados: {data_invertida}')
print("==============================")