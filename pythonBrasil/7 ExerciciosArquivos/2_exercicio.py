'''
    A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
    Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
    e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet,
    ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

            alexandre       456123789
            anderson        1245698456
            antonio         123456456
            carlos          91257581
            cesar           987458
            rosemary        789456125

    Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa
    que gere um relatório, chamado "relatório.txt", no seguinte formato:

            ACME Inc.               Uso do espaço em disco pelos usuários
            ------------------------------------------------------------------------
            Nr.  Usuário        Espaço utilizado     % do uso

            1    alexandre       434,99 MB             16,85%
            2    anderson       1187,99 MB             46,02%
            3    antonio         117,73 MB              4,56%
            4    carlos           87,03 MB              3,37%
            5    cesar             0,94 MB              0,04%
            6    rosemary        752,88 MB             29,16%

    Espaço total ocupado: 2581,57 MB
    Espaço médio ocupado: 430,26 MB
    O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários,
    de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes
    deverá ser feita através de uma função separada, que será chamada pelo programa principal.
    O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo
    programa principal.
'''


def conv_bytes_to_mb(bytes):
    return int(bytes) / 1_048_576


lista_de_dados = []

with open('usuarios.txt', 'r') as arquivo_usuario:          #lê o arquivo usuarios.txt
    for linha in arquivo_usuario:
        linha = linha.strip()
        usuario = linha[:15]                                # 15 primeiros chars
        bytes_consumidos = conv_bytes_to_mb(linha[16:])     # imprime depois dos 15 primeiros chars
        lista_de_dados.append((usuario, bytes_consumidos))

cabecalho = '''
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso\n
'''

with open('relatorio.txt', 'w') as arquivo_relatorio:
    arquivo_relatorio.writelines(cabecalho)
    espaco_total_ocupado = sum([tamanho for _, tamanho in lista_de_dados])  # soma os valores consumidos em MB
    media = espaco_total_ocupado / len(lista_de_dados)
    for indice, dados in enumerate(lista_de_dados):
        usuario, bytes_consumidos = dados                                   # desempacotar a lista
        arquivo_relatorio.writelines(
            f'{indice + 1:<4} {usuario} {bytes_consumidos:9.2f} MB         {bytes_consumidos / espaco_total_ocupado:.2%}\n')

    arquivo_relatorio.writelines(f'\nEspaço total ocupado: {espaco_total_ocupado:.2f} MB')
    arquivo_relatorio.writelines(f'\nEspaço médio ocupado: {media:.2f} MB')
