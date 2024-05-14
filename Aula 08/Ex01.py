#Exercicio 01 - Elabore um algoritmo para ler/receber, separadamente, o
##primeiro nome, o nome do meio e o sobrenome de uma pessoa.
##Em seguida, mostre o nome completo, correspondente.


num1 = input("Digite seu primeiro nome: ")
num2 = input("Digite o seu nome do meio: ")
num3 = input("Digite o seu sobrenome: ")

nome = num1 + " " + num2 + " " + num3 + "."

print("====================================")
print(f"Olá! Seja bem vindo {nome}")
print("====================================")

