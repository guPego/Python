print("Fazenda de rabbits", "\n")

quantMes = int(input("Filhotes depois de quantos meses ? "))

mes, mesSeguinte = 1, 1

if quantMes <= 2:
    print("Coelhos não reprocriaram")
elif quantMes > 2:
    for i in range(2, quantMes):
        coelhos = mes + mesSeguinte;
        mesSeguinte = mes;
        mes = coelhos;
    print("O número total de coelhos é: ", coelhos)

