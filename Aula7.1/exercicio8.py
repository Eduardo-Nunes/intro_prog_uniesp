def bin(decimal):
    binario = []
    str_bin = ""
    while decimal > 0:
        binario.append(str(decimal%2))
        decimal = decimal // 2
    for c in reversed(binario):
        str_bin += c
    return str_bin

numero = int(input("Digite um número decimal: "))
binario = bin(numero)
print(f"O numero {numero} em binario = {binario}")