def titulo(a, n):
    print("-" * n)
    print(f"{a:^{n}}")
    print("-" * n)


def metade(a, f=False):
    b = a/2
    if f:
        b = moeda(b)
    return b


def dobro(a,f=False):
    b = a * 2
    if f:
        b = moeda(b)
    return b


def aumentar(a, c, f=False):
    b = a * (c/100)
    c = a + b
    if f:
        c = moeda(c)
    return c


def diminuir(a, c,f=False):
    b = a * (c/100)
    c = a - b
    if f:
        c = moeda(c)
    return c


def moeda(a):
    b = f"R${a:.2f}"
    return b


def resumo(a=0, b=0, c=0):
    titulo("RESUMO DO VALOR")
    print(f"valor analisado: \t{moeda(a)}")
    print(f"dobro do valor: \t{dobro(a, True)}")
    print(f"metade do valor: \t{metade(a, True)}")
    print(f"{b}% de aumento: \t{aumentar(a, b,True)}")
    print(f"{c}% de diminuição: \t{diminuir(a, c,True)}")
    print("-" * (len("RESUMO DO VALOR") + 20))