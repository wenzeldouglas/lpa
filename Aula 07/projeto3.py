soma = 0
idade = 100
qtd = 0

while idade != 0:
    idade = int(input(f'Digite a idade do aluno {qtd+1}: '))
    if idade != 0:
        soma = soma + idade
        qtd = qtd + 1
media = soma / qtd
print(f'A média das idades é: {media} anos')