'''
    Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
    contendo um relatório dos endereços IP válidos e inválidos.

    O arquivo de entrada possui o seguinte formato:
        200.135.80.9
        192.168.1.1
        8.35.67.74
        257.32.4.5
        85.345.1.2
        1.2.3.4
        9.8.234.5
        192.168.0.256

        O arquivo de saída possui o seguinte formato:
            [Endereços válidos:]
            200.135.80.9
            192.168.1.1
            8.35.67.74
            1.2.3.4

            [Endereços inválidos:]
            257.32.4.5
            85.345.1.2
            9.8.234.5
            192.168.0.256
'''


def validar(ip: str) -> bool:
    numeros = ip.split('.')

    if len(numeros) != 4:  # IP diferente de 4 retorna Falso
        return False

    for n in numeros:
        if not (0 <= int(n) <= 255):  # se o IP nao esta dentro do intervalo de 0 a 255
            return False

    return True


ips_validos = []
ips_invalidos = []
with open('ips.txt', 'r') as arquivo:  # le um arquivo
    for ips in arquivo:
        ip = ips.strip()  # strip remove todos os caracteres especias como o pular linhas e espaços
        if validar(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)

with open('ips_saida.txt', 'w') as arquivo:
    arquivo.writelines('[Endereços válidos:]\n')

    for ip in ips_validos:
        arquivo.writelines(f'{ip}\n')

    arquivo.writelines('\n')
    arquivo.writelines('\n')
    arquivo.writelines('[Endereços inválidos:]\n')

    for ip in ips_invalidos:
        arquivo.writelines(f'{ip}\n')
