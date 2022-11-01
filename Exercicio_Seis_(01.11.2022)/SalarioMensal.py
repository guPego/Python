print("Salário", "\n")

salarioHora = float(input("Salário/Hora: "))
horaMensal = float(input("Horas mensal: "))
print("")

salarioBruto = float(salarioHora * horaMensal)

print("Folha de pagamento")
print("Salário bruto: ", salarioBruto)
impostoINSS = salarioBruto * 0.08; print("INSS: ", impostoINSS)
impostoSindicado = salarioBruto * 0.05; print("Sindicado: ", impostoSindicado)
impostoIR = salarioBruto * 0.11; print("IR: ", impostoIR)
print("Salário líquido: ", salarioBruto - impostoINSS - impostoSindicado - impostoIR)

