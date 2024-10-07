def mensagem(msg, l='-'):
    tam = 38
    print(l*tam)
    print(f'{msg:^{tam}}')
    print(l*tam)

c = ('\033[m',
       '\033[33m',
       '\033[36m',
       '\033[31m')


def menu(opc):
    mensagem('MENU PRINCIPAL')
    for pos, o in enumerate(opc):
        pos += 1
        print(f'{c[1]}{pos}{c[0]} - {c[2]}{o}{c[0]}')
    print('-'*38)

def leia_int(txt):
    try:
        n = int(input(txt))
    except ValueError:
        print(f'{c[3]}ERRO digite um valor válido{c[0]}')
    else:
        return n