
print("Informe a seguir o turno em que estuda")
turno = input("M para matutino, V para vespertino e N para noturno: ")

match turno:
    case "M" | "m":
        print("Bom dia")
    case "V" | "v":
        print("Boa tarde!")
    case "N" | "n":
        print("Boa noite!")
    case _:
        print("Valor digitado inválido.")