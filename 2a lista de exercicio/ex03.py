#Aluno: Douglas Victor Wenzel Nunes | RA: 3011392413022
#Segunda lista de exercícios - Lógica de Programação e Algorítimos | Prof. Piva.
    #3) Receba como entrada um número positivo no formato de String.
    #Dois valores devem ser devolvidos: a soma total de todos os digitos deste número e
    #o valor da multiplicação de todos esses mesmos dígitos.
ra =input("Digite um numero positivo: ")

tupla_str = tuple(ra)
tupla_int = tuple(map(int, tupla_str))

soma = sum(tupla_int)
multiplicacao = 1

for i in tupla_int:
    multiplicacao = multiplicacao * i

print(f"O valor da soma dos digitos é igual a  {soma}")
print(f"O valor da multiplicação dos digitos é igual a {multiplicacao}")
