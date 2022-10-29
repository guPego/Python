print("Somatório de notas")
print("Prova nota mínima e máxima: 0 - 10")
print("Trabalho nota mínima e máxima: 0 - 15")
print("")

provaBimestreUm = float(input("Prova 1º bimestre: "))
while(provaBimestreUm > 10 or provaBimestreUm < 0):
    provaBimestreUm = float(input("Valor inválido, digite novamente: "))
trabalhoBimestreUm = float(input("Trabalho 1º bimestre: "))
while(trabalhoBimestreUm > 15 or trabalhoBimestreUm < 0):
    trabalhoBimestreUm = float(input("Valor inválido, digite novamente: "))
primeiroBimestre = float(provaBimestreUm + trabalhoBimestreUm)

provaBimestreDois = float(input("Prova 2º bimestre: "))
while(provaBimestreDois > 10 or provaBimestreDois < 0):
    provaBimestreDois = float(input("Valor inválido, digite novamente: "))
trabalhoBimestreDois = float(input("Trabalho 2º bimestre: "))
while(trabalhoBimestreDois > 15 or trabalhoBimestreDois < 0):
    trabalhoBimestreDois = float(input("Valor inválido, digite novamente: "))
segundoBimestre = float(provaBimestreDois + trabalhoBimestreDois)

provaBimestreTres = float(input("Prova 3º bimestre: "))
while(provaBimestreTres > 10 or provaBimestreTres < 0):
    provaBimestreTres = float(input("Valor inválido, digite novamente: "))
trabalhoBimestreTres = float(input("Trabalho 3º bimestre: "))
while(trabalhoBimestreTres > 15 or trabalhoBimestreTres < 0):
    trabalhoBimestreTres = float(input("Valor inválido, digite novamente: "))
terceiroBimestre = float(provaBimestreTres + trabalhoBimestreTres)

provaBimestreQuatro = float(input("Prova 4º bimestre: "))
while(provaBimestreQuatro > 10 or provaBimestreQuatro < 0):
    provaBimestreQuatro = float(input("Valor inválido, digite novamente: "))
trabalhoBimestreQuatro = float(input("Trabalho 4º bimestre: "))
while(trabalhoBimestreQuatro > 15 or trabalhoBimestreQuatro < 0):
    trabalhoBimestreQuatro = float(input("Valor inválido, digite novamente: "))
quatroBimestre = float(provaBimestreQuatro + trabalhoBimestreQuatro)

notaTotal = float(primeiroBimestre + segundoBimestre + terceiroBimestre + quatroBimestre)

if(notaTotal >= 60):
    print("Aluno aprovado com a nota", notaTotal)
elif(notaTotal < 40):
    print("Aluno reprovado sem chance à recuperação")
else:
    print("Aluno em recuperação")

