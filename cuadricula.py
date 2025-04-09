import os

dimensiones = {
    "col": os.get_terminal_size().columns,
    "lines": os.get_terminal_size().lines,
}

def cuadricula():
    cont1 = "Contador 1: []"
    cont2 = "Contador 2: []"
    col = dimensiones["col"]
    lines = dimensiones["lines"]
    margen = 2

    print(cont1 + cont2.rjust(col - len(cont1)), end="")
    print("╔" + ("═" * (col - margen)) + "╗", end="")
       
    for i in range(lines - 2):
        print( "║" + ("*" * (col - margen) + "║"), end="")

    print("╚" + ("═" * (col - margen)) + "╝", end="")
    print("Registro 1: ")
    print("Registro 2: ")
    print("Registro 3: ")

cuadricula()

