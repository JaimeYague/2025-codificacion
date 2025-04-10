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


def registros(lista):
    for i in lista:
        print(i)


def ejemplo():
    col, lines, cont1, cont2 = dimensiones()
    cuadricula(col, lines, cont1, cont2)
    registros([
        "Registro 1: ",
        "Registro 2: ",
        "Registro 3: ",
    ])

    
if __name__ == "__main__":

    ejemplo()
