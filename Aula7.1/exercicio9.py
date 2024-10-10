def triangulo(tamanho):
    for i in range(tamanho):
        print(" " * (tamanho - i - 1) + "#" * (2 * i + 1))

def quadrado(tamanho):
    for i in range(tamanho):
        print("#" * tamanho)

def losango(tamanho):
    for i in range(tamanho):
        print(" " * (tamanho - i - 1) + "#" * (2 * i + 1))
    for i in range(tamanho - 2, -1, -1):
        print(" " * (tamanho - i - 1) + "#" * (2 * i + 1))
        

triangulo(3)
quadrado(4)
losango(5)