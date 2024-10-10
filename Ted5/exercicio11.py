def escolher_governante(notas_candidato1, notas_candidato2, notas_candidato3):
    # Calculando as médias
    media1 = sum(notas_candidato1) / len(notas_candidato1)
    media2 = sum(notas_candidato2) / len(notas_candidato2)
    media3 = sum(notas_candidato3) / len(notas_candidato3)
    
    # Encontrando a maior média
    maior_media = max(media1, media2, media3)
    
    # Verificando se há empate
    vencedores = []
    if media1 == maior_media:
        vencedores.append("Candidato 1")
    elif media2 == maior_media:
        vencedores.append("Candidato 2")
    elif media3 == maior_media:
        vencedores.append("Candidato 3")
        
    # Exibindo o resultado
    if len(vencedores) == 1:
        print(f"O vencedor é: {vencedores[0]}")
    else:
        print("Houve empate entre:", ", ".join(vencedores))
        
def receber_notas(candidato):
    notas = []
    while len(notas) < 4:
        nota = int(input(f"Digite a nota {len(notas) + 1} do {candidato} : "))
        notas.append(nota)
    return notas
        

def main ():
    notas_candidato1 = receber_notas("Candidato 1")
    notas_candidato2 = receber_notas("Candidato 2")
    notas_candidato3 = receber_notas("Candidato 3")

    escolher_governante(notas_candidato1, notas_candidato2, notas_candidato3)
    
if __name__ == "__main__":
    main()