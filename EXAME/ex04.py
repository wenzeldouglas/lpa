carro = input("Digite o nome carro: ")
preco_fabrica = int(input("Digite o preço de fábrica: "))

print("Calculando...")
impostos = preco_fabrica * 0.45
lucro_revendedor =  preco_fabrica * 0.28
preco_final = preco_fabrica + impostos + lucro_revendedor
print(f"Automóvel: {carro.upper()}")
print(f"Preço de Fábrica:.: {round(preco_fabrica)}")
print(f"Impostos..........: {round(impostos)}")
print(f"Lucro Revendedor..: {round(lucro_revendedor)}")
print(f"Preço Final.......: {round(preco_final)}")