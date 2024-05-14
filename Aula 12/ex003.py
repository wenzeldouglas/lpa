def conversor(h, m, s):
    h1 = (h*60) * 60
    m1 = m*60
    total = h1 + m1 + s
    return total

print(f"Conversor de Horas, Minutos e Segundos para segundos")
x = int(input("Digite a quantidade de horas: "))
y = int(input("Digite a quantidade de minutos: "))
z = int(input("Digite a quantidade de segundos: "))

verif = int(input(f'Você está querendo converter {x}h {y}min e {z}s em segundos? Digite 0 para sim '))
if verif == 0:
    print(f'O total deste tempo é {conversor(x,y,z)} segundos')