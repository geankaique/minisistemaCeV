from tools import *
from arquivo import *
from time import sleep

arq = 'database.txt'

if not verificar_arquivo(arq):
    criar_arquivo(arq)

opcao = ['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Limpar banco de dados','Sair do Sistema']

while True:
    menu(opcao)
    opc = leia_int(f'{c[1]}Sua opção: {c[0]}')
    if opc == 1:
        mensagem('Listando pessoas...')
        ler_arquivo(arq)
        sleep(2)
    elif opc == 2:
        mensagem('Cadastrando pessoas...')
        nome = input('Nome: ')
        idade = leia_int('Idade: ')
        cadastrar(arq,nome,idade)
    elif opc == 3:
        mensagem('Limpando banco dados...')
        limpar_arquivo(arq)
        sleep(1)
    elif opc == 4:
        mensagem('Finalizando programa...')
        break
    else:
        print(f'{c[3]}ERRO opção Inválida!{c[0]}')