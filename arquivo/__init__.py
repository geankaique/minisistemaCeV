def verificar_arquivo(txt):
    try:
        a = open(txt, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(txt):
    try:
        a = open(txt, 'wt+')
    except Exception as e:
        print(f'Erro ao criar o arquivo {e}')
    else:
        a.close()

def cadastrar(txt, nome, idade):
    try:
        a = open(txt, 'at')
    except Exception as e:
        print(f'ERRO {e}')
    else:
        a.write(f'{nome};{idade}\n')
        a.close()

def ler_arquivo(arq):
    try:
        a = open(arq,'rt')
    except Exception as e:
        print(f'Erro ao Ler arquivo {e}')
    else:
        for linha in a:
            dados = linha.split(';')
            nome = dados[0]
            idade = dados[1].replace('\n', '')
            print(f'{nome:<20}{idade} anos')

def limpar_arquivo(arq):
    try:
        a = open(arq, 'w')
    except Exception as e:
        print(f'Erro ao abrir arquivo: {e}')
    else:
        a = a.write('')