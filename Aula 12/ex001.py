def e_par(n):
    if n%2 == 0:
        return True
    return False

x = int(input("Digite um valor: "))
if e_par(x):
    print(f"O valor {x} é um número Par!")
else:
    print(f"O valor {x} é um número Impar!")