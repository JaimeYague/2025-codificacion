import os

dimensiones = {
    "col": os.get_terminal_size().columns,
    "lines": os.get_terminal_size().lines,
}

def cuadricula():
    col = dimensiones["col"]
    lines = dimensiones["lines"]
    cont1 = "Contador Izq.: " + str(col)
    cont2 = "Contador Der.: " + str(lines)
    
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

