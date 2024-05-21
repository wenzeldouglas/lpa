#Aluno: Douglas Victor Wenzel Nunes | RA: 3011392413022
#Segunda lista de exercícios - Lógica de Programação e Algorítimos | Prof. Piva.
    #1) Em um cercado existem vários patos e coelhos. Escreva uma função que recebe como parâmetro
    #o total de cabeças e o total de pés e retorne dois valores: o total de patos e
    #o total de coelhos que se encontram nesse cercado.

def calcular(cabecas, pes):
    coelhos = (pes - 2 * cabecas) / 2
    patos = cabecas - coelhos
    print("Total de patos:", patos)
    print("Total de coelhos:", coelhos)
print("=================================================================")

y = int(input("Digite os dois últimos dígitos do seu RA: "))
cabecas = y
pes = y*3+3

print(f"Quantidade de cabeças: {cabecas}")
print(f"Quantidade de pés: {pes}")
print("=========================[Uso da função]=========================")
calcular(cabecas, pes)