def validadorCPF(cpf):


    def calcula_digito(cpf, peso):
        soma = sum(int(c) * p for c, p in zip(cpf, peso))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    if len(cpf) != 11:
        return False

    peso1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    peso2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    digito1 = calcula_digito(cpf[:9], peso1)
    digito2 = calcula_digito(cpf[:10], peso2)

    return int(cpf[9]) == digito1 and int(cpf[10]) == digito2

# Teste
print('CPF Válido!') if validadorCPF('54647142949') else print('CPF Inválido!')
print('CPF Válido!') if validadorCPF('54747142949') else print('CPF Inválido!')
print('CPF Válido!') if validadorCPF('17824630706') else print('CPF Inválido!')
print('CPF Válido!') if validadorCPF('17824630806') else print('CPF Inválido!')
