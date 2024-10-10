N = int(input("Digite o quantidade de numero da Sequencia de Fibonacci que deseja: "))
sequencia = []

if N == 1:
    sequencia = [0]  
elif N > 1:
    sequencia = [0, 1]

while len(sequencia) < N:
    l = len(sequencia)
    t = sequencia[l-1] + sequencia[l-2]
    sequencia.append(t)

for i in sequencia:
    print(i)