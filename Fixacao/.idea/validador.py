ef valida_cpf(cpf):
    # Remover pontos e traço do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcular o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito_1 = 11 - (soma % 11)
    if digito_1 > 9:
        digito_1 = 0

    # Calcular o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito_2 = 11 - (soma % 11)
    if digito_2 > 9:
        digito_2 = 0

    # Verificar se os dígitos verificadores estão corretos
    if int(cpf[9]) == digito_1 and int(cpf[10]) == digito_2:
        return True
    else:
        return False

# Teste da função
if __name__ == "__main__":
    cpf = "123.456.789-09"  # Coloque um CPF válido ou inválido para testar
    if valida_cpf(cpf):
        print("CPF válido")
    else:
        print("CPF inválido")