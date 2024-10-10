def primo(number):
    if number < 0:
        return False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True
    
if __name__ == '__main__':
    n = int(input("Digite o numero: "))
    if primo(n):
        print("Esse numero é primo")
    else:
        print("Esse numero não é primo")