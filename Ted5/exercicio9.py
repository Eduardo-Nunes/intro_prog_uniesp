print("1 para feitiço de Fogo")
print("2 para feitiço de Agua")
print("3 para feitiço de Terra")
feitico = int(input("Digite qual o numero do feitiço que deseja escolher:"))
magia = ""

match feitico:
    case 1:
        magia = "Fogo"
    case 2:
        magia = "Agua"
    case 3:
        magia = "Terra"

print(f"Sua magia de {magia} está pronta")