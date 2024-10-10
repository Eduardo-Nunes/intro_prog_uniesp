moeda_1_real = int(input("Digite o número de moedas de 1 Real: "))
moeda_50_cents = int(input("Digite o número de moedas de 50 Centavos: "))
moeda_25_cents = int(input("Digite o número de moedas de 25 Centavos: "))

valor_50_cents = moeda_50_cents * 0.5
valor_25_cents = moeda_25_cents * 0.25

print(f"Valor total: {moeda_1_real + valor_50_cents + valor_25_cents}")
print(f"{moeda_1_real}R$ em modeas de 1 Real")
print(f"{valor_50_cents}R$ em moedas de 50 Centavos")
print(f"{valor_25_cents}R$ em moedas de 25 Centavos")