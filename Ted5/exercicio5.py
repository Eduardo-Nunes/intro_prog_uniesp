distancia = float(input("Digite a distancia em quilometros que ainda falta para chegar no oasis: "))
l_agua = float(input("Digite a quantidade de litros de agua restante: "))

dis_maxima = l_agua/2

if(distancia <= dis_maxima) :
    print("Você possui agua suficiente para a distancia a percorrer ")
else :
    print("Você NÂO possui agua suficiente")