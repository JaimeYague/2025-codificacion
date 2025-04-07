def asciilist():
    listaascii = list(range(31, 256))
    columnas = 5

    for i in listaascii:
        number = str(i).ljust(3)
        caracter = chr(i).ljust(1, "|")
        print("|", number,"==", caracter, end=" | ")
        if not (i % columnas):
            print()

if __name__ == "__main__":
    asciilist()