import random

numero_sorteado = random.randint(1,100)
tentativas = 0
while True:
    numero_escolhido = int(input("tente adivinhar o numero de 1 a 100 ou -1 para desistir: "))
    tentativas += 1
    if numero_escolhido < 0:
        print("Fez bem em assumir a sua mediocridade")
        break
    elif numero_escolhido == numero_sorteado:
        print(f"Caraca mano tu é foda! Acertou após {tentativas} tentativas")
        break
    elif numero_sorteado > numero_escolhido:
        print("A gnt ta lascado, o numero é Maior!")
    elif numero_escolhido > numero_sorteado:
        print("Calma ai Calabreso, o numero é Menor!")