def leiadinheiro(a):
    from Funções.utilidadesCeV import cores
    while True:
        b = str(input(a)).strip()
        b = b.replace(",", ".")
        d = b[:]
        d = d.replace(".", "")
        if not d.isnumeric():
            print(f'{cores.cor(1, "vermelho")} "{b}" é um preço invalido, por favor tente novamente: {cores.cor(1, "sem_cor")}')
        if d.isnumeric():
            break
    return float(b)


def leiaInt(arg):
    from Funções.utilidadesCeV.cores import cor
    while True:
        try:
            a = int(input(arg))
        except KeyboardInterrupt:
            print(f'\n{cor(1, "vermelho")}O usuario preferiu não digitar esse numero.{cor(1, "sem_cor")}')
            return 0
            break
        except (ValueError, TypeError):
            print(f'{cor(1, "vermelho")}ERRO: por favor, Digite um numero interio valido{cor(1, "sem_cor")}')
            continue
        else:
            return a
            break


def leiaFloat(arg):
    from Funções.utilidadesCeV.cores import cor
    while True:
        try:
            a = float(input(arg))
        except KeyboardInterrupt:
            print(f'\n{cor(1, "vermelho")}O usuario preferiu não digitar esse numero.{cor(1, "sem_cor")}')
            return 0
            break
        except (ValueError, TypeError):
            print(f'{cor(1, "vermelho")}ERRO: por favor, Digite um numero real valido{cor(1, "sem_cor")}')
            continue
        else:
            return a
            break


def menu(arg, n, a, args):
    from Funções.utilidadesCeV.cores import cor
    from Funções.utilidadesCeV.moedas import titulo
    while True:
        titulo('MENU PRINCIPAL', n)
        print(args)
        print('-' * n)
        try:
            op = int(input(arg))
        except KeyboardInterrupt:
            print(f'\n{cor(1, "vermelho")}ERRO: o usuario decidiu parar o programa!!{cor(1, "sem_cor")}')
        except (ValueError, TypeError):
            print(f'{cor(1, "vermelho")}ERRO: por favor digite um valor inteiro valido{cor(1, "sem_cor")}')
        else:
            if op > a or op < 1:
                print(f'{cor(1, "vermelho")}ERRO: por favor digite uma opção valida{cor(1, "sem_cor")}')
            else:
                break
    print('-' * n)
    return op
