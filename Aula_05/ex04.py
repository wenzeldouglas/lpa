a = int(input("Digite o primeiro lado do triangulo: "))
b = int(input("Digite o segundo lado do triangulo: "))
c = int(input("Digite o terceiro lado do triangulo: "))

if ((a+b) < c) or ((b+c) < a) or ((a+c) < b):
    print("Não é um triângulo!")
elif (a == b) and (b == c):
    print("Triângulo Equilátero")
elif (a == b) or (b == c) or (c == a):
    print("Triângulo Isósceles")
elif (a != b) and (b != c):
    print("Triângulo Escaleno")