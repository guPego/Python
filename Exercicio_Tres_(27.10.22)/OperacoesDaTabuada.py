numero = int(input("Digite um número inteiro para a tabuada: "))
intervaloFim = int(input("Digite o ultímo número a ser multiplicado: "))

for i in range(intervaloFim):
    numeroMultiplicado = numero * i;
    print(numero, " * ", i, " = ", numeroMultiplicado);