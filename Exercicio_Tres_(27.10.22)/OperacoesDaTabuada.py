numero = int(input("Digite um número inteiro para a tabuada: "))
intervaloFim = int(input("Digite até que número será multiplicado: "))

for i in range(intervaloFim):
    numeroMultiplicado = numero * i;
    print(numero, " * ", i, " = ", numeroMultiplicado);
