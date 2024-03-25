larg = float(input("Digite a largura do aposento: "))
comp = float(input("Digite o comprimento do aposento: "))
tinta = int(input("Digite a quantidade de litros de tinta disponível: "))
porta = 1.68
alt = 2.8

larg2 = larg * alt
comp2 = comp * alt
total = (larg2 + comp2) - porta
total = total / 3

if tinta >= total:
    print(f'Serão necessários {total:2f} litros de tinta para pintar o aposento. Você tem o suficiente')
else:
    print(f'Serão necessários {total:2f} litros de tinta para pintar o aposento. Você NÃO tem o suficiente')