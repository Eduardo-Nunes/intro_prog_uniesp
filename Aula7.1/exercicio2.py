def tabuada(numero):
    print(f"Tabuada de {numero} :")
    for i in range(1,11):
        print(f'{numero} x {i} = {numero * i}')
        

if __name__ == '__main__':
    numero = int(input("Digite o número que deseja ver a Tabuada: "))
    tabuada(numero)