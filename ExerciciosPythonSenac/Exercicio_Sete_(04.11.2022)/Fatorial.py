print("Fatorial de número inteiro")

def fatorial(n):
    if n <= 1:
        return 1;
    else:
        return n * fatorial(n - 1)

fator = int(input("Digite um número para ser fatorado: "))

print(f"O número {fator} fatorado é: {fatorial(fator)}")
