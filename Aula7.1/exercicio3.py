palavra = input("Digite a palavra: ").lower()
vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"
n_vogais = 0
n_consoantes = 0
for c in palavra:
    if c in vogais:
        n_vogais += 1
    elif c in consoantes: 
        n_consoantes += 1
        
print(f"A palavra tem {n_vogais} vogais e {n_consoantes} consoantes")