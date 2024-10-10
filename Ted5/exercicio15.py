import os
clear = lambda: os.system('cls')

def carimbador_maluco(energia, coordenadas, tempo):
    aprovado = True
    if energia < 80:
        print("Nivel de energia abaixo do esperado!")
        aprovado = False
    if len(coordenadas) < 2 :
        print("Está faltando as Coordenadas!")
        aprovado = False
    if tempo == 0 :
        print("Está faltando o Ano para o qual deseja ir!")
        aprovado = False
    
    return aprovado
    

if __name__ == '__main__':
    option = 1
    energia = 0
    coordenadas = []
    tempo = 0
    pode_partir = False
    while option > 0 :
        clear()
        pode_partir = carimbador_maluco(energia, coordenadas, tempo)
        
        if pode_partir:
            print("Tudo Okay para a viagem!")
        else:
            print("Não vai Viajar!")
        
        print("Opções:")
        print("2 - Recarregar Energia")
        print("3 - Inserir Coordenadas")
        print("4 - Ajustar Ano de chegada")
        if pode_partir :
            print("5 - Pau na maquina e sair fora!")
            
        print("0 - Sair")
        option = int(input("Digite uma das opçoes para realizar uma ação: "))
        
        match option:
            case 2:
                energia = int(input("Digite o nível de energia da maquina: "))
            case 3:
                x = float(input("Digite a Coordenada X: "))
                y = float(input("Digite a Coordenada Y: "))
                coordenadas = [x, y]
            case 4:
                tempo = int(input("Digite o ano que deseja ir: "))
            case 5:
                print("Valeu Falou!")
                option = 0
        
    print('--- --- This is the End --- ---')