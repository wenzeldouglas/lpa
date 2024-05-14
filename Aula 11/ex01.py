dict = {}

for x in range(3):
    sobrenome = input("Digite seu sobrenome: ")
    idade = int(input("Digite a sua idade: "))
    dict[sobrenome] = idade

maisvelho = max(dict, key=dict.get)
print(f'A pessoa mais velha é a {maisvelho}')

