print("Três vetores")
print("")

vetorUm = []
for i in range(10):
    vetorUm.append(input("Digite um número para a posição " +str(i)+ " do primeiro vetor: "))

print("")

vetorDois = []
for i in range(10):
    vetorDois.append(input("Digite um número para a posição " +str(i)+ " do segundo vetor: "))

print("")

vetorTres = []
for i, j in zip(vetorUm, vetorDois):
    vetorTres.append(i)
    vetorTres.append(j)
print("Terceiro vetor: ", vetorTres)