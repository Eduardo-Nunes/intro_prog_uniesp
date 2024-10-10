inputed = 0
notas = []
while inputed >= 0:
    inputed = float(input("Digite a nota ou -1 para sair: "))
    if inputed >= 0 :
        notas.append(inputed)

media = sum(notas)/len(notas)
print(f"Media do Aluno foi {media}")