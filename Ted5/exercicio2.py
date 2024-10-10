ouro = int(input("Digite a quantidade de ouro utilizada em Kg: "))
ferro = int(input("Digite a quantidade de ferro utilizada em Kg: "))

p_ferro = (ferro/(ouro + ferro))*100

print(f"Ferro -> {ferro}Kg ")
print(f"Ouro -> {ouro}Kg ")
print(f"Total -> {ferro + ouro}Kg ")
print(f"Porcetagem de ferro {p_ferro}%")

if(p_ferro >= 70) :
    print("Porcentagem de ferro é suficiente")
else :
    print("Porcentagem de ferro é insuficiente")