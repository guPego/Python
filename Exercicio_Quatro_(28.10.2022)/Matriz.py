print("Matriz")
print("")

lista = [[0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4]]

for i in range(5):
    for j in range(5):
        lista[i][j] = int(input("Digite um valor para a linha " + str(i) + " e coluna " + str(j) + ": "))

numeroAleatorio = int(input("Digite um número para ser caçado na lista: "))
numeroNaoEncontrado = True

for i in range(5):
    for j in range(5):
        if(lista[i][j] == numeroAleatorio):
            print("")
            print("Número " + str(numeroAleatorio) + " encontrado na linha " + str(i) + " na coluna " + str(j) + "!")
            numeroEncontrado = False
            break


if(numeroEncontrado == True):
    print("")
    print("Número não encontrado")