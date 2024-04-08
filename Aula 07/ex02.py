altura = 0
peso = 0
menor_imc = 100
maior_imc = 0
peso_soma = 0
altura_soma = 0
for i in range(1,6):
    peso = float(input(f"Digite o peso da pessoa {i}: "))
    altura = float(input(f"Digite a altura da pessoa {i}: "))
    altura_soma = altura + altura
    imc = peso / (altura * altura)
    if imc > maior_imc:
        maior_imc = imc
    elif imc < menor_imc:
        menor_imc = imc
    peso_soma = peso_soma + peso
    altura_soma = altura_soma + altura

print(f"O maior IMC é: {maior_imc:5.2f}")
print(f'O menor IMC é: {menor_imc:5.2f}')
print(f'O peso peso médio é:{peso_soma / 5:5.2f}')
print(f'A altura média é: {altura_soma / 5:5.2f}')




