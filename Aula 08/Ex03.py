#Elabore um algoritmo para determinar quantas vogais existem
#dentro de uma determinada frase (que deve ser recebida do
#usuário).

frase = input("Digite uma frase: ")

vog = 0
cons = 0

for caractere in frase:
    if caractere in 'aeiouAEIOU':
        vog = vog + 1
    else:
        cons = cons + 1

print("=============================")
print(f'Na frase digitada, há {vog} vogais!')
print(f'Na frase digitada, há {cons} consoantes!')
print("=============================")