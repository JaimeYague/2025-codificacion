import os


def dimensiones():
    dimensiones = {
        "col": os.get_terminal_size().columns,
        "lines": os.get_terminal_size().lines,
    }
    col = dimensiones["col"]
    lines = dimensiones["lines"]

    cont1 = "Contador Izq.: " + str(col)
    cont2 = "Contador Der.: " + str(lines)

    return col, lines, cont1, cont2


def cuadricula(col, lines, cont1, cont2):   
    margen = 2

    print(cont1 + cont2.rjust(col - len(cont1)), end="")
    print("╔" + ("═" * (col - margen)) + "╗", end="")
       
    for i in range(lines - 2):
        print( "║" + ("*" * (col - margen) + "║"), end="")

    print("╚" + ("═" * (col - margen)) + "╝", end="")

    return cont1, cont2, col, lines


def registros():
    print("Registro 1: ")
    print("Registro 2: ")
    print("Registro 3: ")


def main():
    col, lines, cont1, cont2 = dimensiones()
    cuadricula(col, lines, cont1, cont2)
    registros()

    
if __name__ == "__main__":

    main()
