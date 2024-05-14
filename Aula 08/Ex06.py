#Faça um algoritmo para ler nove caracteres numéricos em uma
#string. Mostre o conteúdo dessa string colando pontos e virgula,
#respectivamente nas posições inteiras e decimais.


num = input("Digite 9 números: ")
verif = num.count(1234567890)
if verif == 9:
    print(f"Número digitado: {num:}")
else:
    print("Número fora dos parâmetros")
