from Funções.utilidadesCeV.dados import menu
from Funções.utilidadesCeV.cores import cor
from Funções.utilidadesCeV.moedas import titulo

arquivo = open('pessoas.txt', 'a')
arquivo.close()

while True:
    # MENU PRINCIPAL
    opçao = menu('Sua opção: ', 50, 4, f'''{cor(1, "azul")}1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do sistema{cor(1, "sem_cor")}''')




    # PESSOAS CADASTRADAS
    if opçao == 1:
        titulo('PESSOAS CADASTRADAS', 50)
        try:
            arquivo = open('pessoas.txt', 'x')
        except:
            arquivo = open('pessoas.txt', 'r')
        for l in arquivo:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<40}{dado[1]:>4} anos')



    # CADASTRAR PESSOAS
    elif opçao == 2:
        titulo('CADASTRAR PESSOA', 50)
        nome = str(input('NOME: '))
        while True:
            try:
                idade = int(input('IDADE: '))
            except:
                print(f'{cor(1, "vermelho")}Digite um numero inteiro valido{cor(1, "sem_cor")}')
                continue
            else:
                break
        arquivo = open('pessoas.txt', 'a')
        pessoa = f'{nome};{idade}\n'
        arquivo.write(pessoa)
        print(f"{cor(1, 'verde')}NOVO REGISTRO ADICIONADO COM SUCESSO{cor(1, 'sem_cor')}")
        arquivo.close()



    # SAIR DO PROGRAMA
    elif opçao == 3:
        print(f"{cor(1, 'vermelho')}SISTEMA ENCERRADO,{cor(1, 'sem_cor')} {cor(1, 'verde')}VOLTE SEMPRE{cor(1, 'sem_cor')}")
        break
