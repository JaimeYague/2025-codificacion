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
    
    print(cont1 + cont2.rjust(col - len(cont1)))
    print("╔" + ("═" * (col - 3)) + "╗")
       
    for i in range(lines - 2):
        print( "║" + ("*" * (col - 3) + "║"))

    print("╚" + ("═" * (col - 3)) + "╝")
    print("Registro 1: ")
    print("Registro 2: ")
    print("Registro 3: ")

cuadricula()

