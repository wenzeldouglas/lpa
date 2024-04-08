frase = input("Digite uma frase: ")
i = 0
for letra in frase:
    if letra in 'aeiouAEIOUéèáàí':
        i = i+1
print(f'Existem {i} vogais na frase')