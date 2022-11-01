print("Pirâmide impressa", "\n")

for i in range(4):
    for j in range(i+1):
        if(i < 3):
            print(i+1, end=" ")
        else:
            print("n", end=" ")
    print("")