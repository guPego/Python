print("Padaria")

print("")

precoPao = float(input("Preço dos pães: "))
print("Tabela de preços dos pâes")
for i in range(1, 51):
    print(i, "- R$ ", f"{precoPao * i:,.2f}")