print("Calculadora de dois números")
resposta = input("Digite se deseja usar a calculadora: ")

while resposta == "Sim" or resposta == "S" or resposta == "sim" or resposta == "s":
    num1 = input("Digite o primeiro numero para a calculadora: ")
    num2 = input("Digite o segundo numero para a calculadora: ")

    print("")
    print("Soma: ", int(num1) + int(num2))
    print("Subtraído: ", int(num1) - int(num2))
    print("Multiplicado: ", int(num1) * int(num2))
    print("Dividido: ", int(num1) / int(num2))

    if(resposta != "Sim" or resposta != "S" or resposta != "sim" or resposta != "s"):
        print("Calculadora fechada")

    print("")
    resposta = input("Digite Sim se deseja continuar usando a calculadora ou Não se deseja parar: ")