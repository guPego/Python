print("Pirâmide impressa", "\n")

num = int(input("Digite um número para finalizar a piramide: "))
print("")

for i in range(4):
    for j in range(i+1):
        if(i < 3):
            print(i+1, end=" ")
        else:
            print("n", end=" ")
    print("")

print("")

for i in range(0, num):
    for j in range(i+1):
        print(i+1, end=" ")
    print("")