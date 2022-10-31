print("Vetor de caracteres")

caracteres = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10):
    caracteres[i] = str(input("Digite uma letra para a posição " + str(i+1) + ": ").lower())
print(caracteres, "\n")

contador = 0

for i in range(10):
    if not (caracteres[i] == str("a") or caracteres[i] == str("e") or caracteres[i] == str("i") or caracteres[i] == str("o") or caracteres[i] == str("u")):
        print("Consoante na posição " + str(i+1) + ": ", caracteres[i])
        contador = contador + 1
print("Totais de consoantes: ", contador)

