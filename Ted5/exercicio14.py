def julgar_duelistas(atq1, atq2, def1, def2) :
    atr1 = atq1 + def1
    atr2 = atq2 + def2
    if atr1 > atr2:
        print("O vencedor do Duelo é o Duelista 1")
    elif atr2 > atr1:
        print("O vencedor do Duelo é o Duelista 2")
    elif def1 > def2:
        print("O vencedor do Duelo é o Duelista 1")
    elif def2 > def1:
        print("O vencedor do Duelo é o Duelista 2")
    else :
        print("Deu Empate!")
        
if __name__ == '__main__':
    # empate
    julgar_duelistas(7,7,7,7)
    # duelista 1
    julgar_duelistas(9,2,2,8)
    #duelista 2 (criterio de defesa)
    julgar_duelistas(4,6,5,6)