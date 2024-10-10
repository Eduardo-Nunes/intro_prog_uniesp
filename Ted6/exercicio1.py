arquivo = open("vingadores.txt", "r")

for linha in arquivo:
    s = len(linha)
    if(linha[s-1] == "\n") :
        convidado = f"{linha[:s-1]}"
    else :
        convidado = linha
            
    mensagem = f"Ola {convidado} \n Você foi convidado para uma festa do Puff, não esqueça o seu óleo de bebê"

    print(mensagem)
    print()
    arquivo_temporario = open(f"Convite para {convidado}", "w")
    arquivo_temporario.write(mensagem)
    arquivo_temporario.close()
    

arquivo.close()