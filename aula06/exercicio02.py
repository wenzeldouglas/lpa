val = float(input("Digite o valor do produto: "))

if (val <= 1000.00):
    novo_val = val - (val*0.1)
    desc = val - novo_val
    print(f'Desconto aplicado de 10%. Parabéns!')
    print(f'R${desc} de desconto aplicado.')
    print(f'Valor a pagar: R${novo_val}')
elif (val <= 5000):
    novo_val = val - (val*0.2)
    desc = val - novo_val
    print(f'Desconto aplicado de 20%. Parabéns!')
    print(f'R${desc} de desconto aplicado.')
    print(f'Valor a pagar: R${novo_val}')
else:
    novo_val = val - (val*0.3)
    desc = val - novo_val
    print(f'Desconto aplicado de 30%. Parabéns!')
    print(f'R${desc} de desconto aplicado.')
    print(f'Valor a pagar: R${novo_val}')