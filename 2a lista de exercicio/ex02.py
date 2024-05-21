#Aluno: Douglas Victor Wenzel Nunes | RA: 3011392413022
#Segunda lista de exercícios - Lógica de Programação e Algorítimos | Prof. Piva.
    #2) Função que determine se um número é primo ou não. Caso for primo,
    #retorna True, se não, False. Implemente outra função que recebe como parâmetro um
    #determinado número inteiro positivo e retorne a quantidade de números primos correspondente
    #ao valor passado por parâmetro, partindo de zero.
    #Os dois últimos números do seu RA é igual a Y.
    #Após, um outro script irá utilizar essas duas funções para devolver uma lista contendo o total
    #de números primos correspondentes a Y*2+5. Em seguida, deve calcular o valor da soma de todos
    #os os números da lista.

def primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
def primeiros(x):
    primos = []
    numero = 0
    while len(primos) < x:
        if primo(numero):
            primos.append(numero)
        numero += 1
    elementos = len(primos)
    print(f"A quantidade de elementos nessa lista é de {elementos}")
    return primos


print("================[Verificar Numero Primo]==================")
verif = int(input("Digite um número para verificação: "))
if primo(verif):
    print(f"{verif} é um número primo")
else:
    print(f"{verif} não é um número primo")


Y = 22
atributo = Y*2+5

print("========[Função Verificar Numero Primo do Usuario]=======")
x = int(input("Digite um valor: "))
print(primeiros(x))
print("=======[Função Verificar Numero primo do Y*2+5]===========")
lista = primeiros(atributo)
print(lista)
print("==========[Soma dos números dentro da lista]==============")
lista_quantidade = sum(lista)
print(f"A soma dos números da lista anterior é igual a {lista_quantidade}")
print("==========================================================")