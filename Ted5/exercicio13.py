import os
clear = lambda: os.system('cls')

def inicializar_defesa() :
    posicao = input("Digite a posição do exercito do rei (dentro ou fora) :")

    match posicao:
        case 'dentro' :
            print("Defesas desativadas")
        case 'fora' :
            print("Defesas Ativadas")
        case _ :
            print("Opção inválida")

if __name__ == '__main__':
    clear()
    option = 1
    
    while option > 0 :
        inicializar_defesa()
        print("Opções:")
        print("1 - Alterar Posição")
        print("0 - Sair")
        option = int(input("Digite uma das opçoes para realizar uma ação: "))
    
    print('--- --- This is the End --- ---')
        
        
        