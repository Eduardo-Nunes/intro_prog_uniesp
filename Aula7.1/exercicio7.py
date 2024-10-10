def fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial


n = int(input("Digite um número: "))
fa = fatorial(n)
print(f"O fatorial de {n} é {fa}")