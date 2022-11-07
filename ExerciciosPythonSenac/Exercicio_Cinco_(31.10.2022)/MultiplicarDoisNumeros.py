print("Multiplicador de dois números", "\n")

numeroUm=float(input("Digite primeiro número: "))
numeroDois=float(input("Digite segundo número: "))

def multiplicaDoisNumeros(n1,n2):
    resultado = n1 * n2
    return print("\n", "O resultado da multiplicação é: ", resultado)

multiplicaDoisNumeros(numeroUm, numeroDois)