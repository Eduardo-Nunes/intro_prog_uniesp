a_t = int(input("Digite qual o tempo do Dragao 1: "))
a_m = int(input("Digite qual a distancia do Dragao 1: "))
b_t = int(input("Digite qual o tempo do Dragao 2: "))
b_m = int(input("Digite qual a distancia do Dragao 2: "))

vel_a = a_m/a_t
vel_b = b_m/b_t

if(vel_a == vel_b) :
    print("O Dragão 1 e o Dragão 2 possuem a mesma velocidade")
elif (vel_b > vel_a) :
    print("O Dragão 2 possui velocidade maior que o Dragão 1")
elif (vel_a > vel_b) :
    print("O Dragão 1 possui velocidade maior que o Dragão 1")