porta = int(input("Escolhar uma porta, digite um numero relacionado de 1 a 5 "))
desafio = ""

match porta :
    case 1:
        desafio = "Enfrentar um Dragão"
    case 2:
        desafio = "Abraçar um Anão"
    case 3:
        desafio = "Acertar um Elfo"
    case 4:
        desafio = "Congelar um Bourog"
    case 5:
        desafio = "Purificar a alma de um Homem"

print(f"Seu desafio é {desafio}")