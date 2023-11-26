import datetime

def formata_data(data):
    data_atual = data
    data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S.%f")[:-3]
    return data_formatada

def formata_e_valida_cpf(cpf):
    cpf_numerico = ''.join(filter(str.isdigit, cpf))

    if len(cpf_numerico) != 11:
        return "CPF inválido. Deve conter 11 dígitos numéricos."

    if cpf_numerico == cpf_numerico[0] * 11:
        return "CPF inválido. Todos os dígitos são iguais."

    cpf_formatado = f"{cpf_numerico[:3]}.{cpf_numerico[3:6]}.{cpf_numerico[6:9]}-{cpf_numerico[9:]}"

    return cpf_formatado