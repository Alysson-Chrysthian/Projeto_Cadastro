def cor(a, b):
    cores_letras = {
    "sem_cor": '\033[m',   #sem cor
    "branco": '\033[30m', #Branco
    "vermelho": '\033[31m', #Vermelho
    "verde": '\033[32m', #Verde
    "amarelo": '\033[33m', #Amarelo
    "azul": '\033[34m', #Azul
    "magenta": '\033[35m', #Magenta
    "ciano": '\033[36m', #Ciano
    "cinza": '\033[37m'  #Cinza
    }

    cores_bg = {
    "sem_cor": '\033[m',   #sem cor
    "branco": '\033[40m', #Branco
    "vermelho": '\033[41m', #Vermelho
    "verde": '\033[42m', #Verde
    "amarelo": '\033[43m', #Amarelo
    "azul": '\033[44m', #Azul
    "magenta": '\033[45m', #Magenta
    "ciano": '\033[46m', #Ciano
    "cinza": '\033[47m'  #Cinza
    }

    if a == 1:
        c = cores_letras[b]
    elif a == 2:
        c = cores_bg[b]
    return c
