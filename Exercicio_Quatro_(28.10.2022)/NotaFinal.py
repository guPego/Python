print("Somatório de notas")

primeiroBimestre = float(input("1º bimestre: "))
while(primeiroBimestre > 25 or primeiroBimestre < 0):
    primeiroBimestre = float(input("Valor inválido, digite novamente: "))

segundoBimestre = float(input("2º bimestre: "))
while(segundoBimestre > 25 or segundoBimestre < 0):
    segundoBimestre = float(input("Valor inválido, digite novamente: "))

terceiroBimestre = float(input("3º bimestre: "))
while(terceiroBimestre > 25 or terceiroBimestre < 0):
    terceiroBimestre = float(input("Valor inválido, digite novamente: "))

quartoBimestre = float(input("4º bimestre: "))
while(quartoBimestre > 25 or quartoBimestre < 0):
    quartoBimestre = float(input("Valor inválido, digite novamente: "))

notaTotal = float(primeiroBimestre + segundoBimestre + terceiroBimestre + quartoBimestre)

if(notaTotal >= 60):
    print("Aluno aprovado com a nota", notaTotal)
elif(notaTotal < 40):
    print("Aluno reprovado sem chance à recuperação")
else:
    print("Aluno em recuperação")

