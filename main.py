def asciilist():
    listaascii = list(range(32, 256))
    qty = 5

    for i in listaascii:
        number = str(i).ljust(3)
        caracter = chr(i).ljust(1, "|")
        print("|", number,"==", caracter, end=" | ")
        if i % qty == 0:
            print()

if __name__ == "__main__":
    asciilist()