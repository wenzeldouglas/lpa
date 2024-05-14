#Exemplo 06 - 8 de abril de 2024

while True:
    idade = (input("Digite sua idade: "))

    if idade.isdigit():
        idade = int(idade)
        print(f'Você tem {idade} anos!')
    else:
        print("Apenas números!")

