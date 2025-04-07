
#Import os Library
import os

# Print the size of terminal
print (os.get_terminal_size())



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

def linea(num: int, qty: int = 5):
    for i in range(qty):
        code = num + i
        print(f"{code}".rjust(3), end="")
        print(": ", end="")
        if code not in [9, 10, 13]:
            print(chr(code), end="")
        else:
            print("*", end="")
        print(" " * 3, end="")
    print()


def main(init: int = 32) -> None:
    qty = 9
    c = init
    while c <= 250:
        linea(c, qty)
        c += qty


if __name__ == "__main__":
    main(0)
