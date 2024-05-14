#Funções com parâmetro padrão
def potencia(numero, expoente = 2):
    resultado = pow(numero, expoente)
    return resultado
#...
n = float(input("Digite o numero: "))
e = int(input("Expoente: "))
print(f"Valor com expoente: {potencia(n,e)}")
print(f"Valor sem o expoente: {potencia(n)}")