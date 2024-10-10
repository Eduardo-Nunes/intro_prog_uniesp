conquistas = int(input("Digite o numero de conquistas do Cavaleiro"))
bonus = 0

if conquistas < 5 :
    bonus = 10
elif conquistas < 10:
    bonus = 50
else :
    bonus = 100
    
print(f"O cavaleiro receberá {bonus} moedas de ouro")