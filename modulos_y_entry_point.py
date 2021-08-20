# ALCANCE globals
numeros = []

def ingresar_numeros():
    opcion = 1
    menu_secundario = """
    (1) Ingresar numero
    (0) Dejar de ingresar numeros
    """
    while opcion > 0:
        print(menu_secundario)
        opcion = int(input("Opcion seleccionada: "))
        if opcion == 1:
            numeros.append(int(input("Ingrese el numero: ")))

def sumar():
    ingresar_numeros()
    total = 0
    for numero in numeros:
        total += numero
    print("El total de la suma es: " + str(total))
    
def restar():
    pass

def multiplicar():
    pass

def dividir():
    pass
    
def menu_principal():
    menu = """
Bienvenido a nuestra calculadora
    (1) Sumar
    (2) Restar
    (3) Multiplicar
    (4) Dividir
    (5) TERMINAR
"""
    opcion = 0
    while opcion < 5:
        print(menu)
        numeros = []
        opcion = int(input("Opcion seleccionada: "))
        if opcion == 1:
            sumar()
        elif opcion == 2:
            restar()
        elif opcion == 3:
            multiplicar()
        elif opcion == 4:
            dividir()

if __name__=="__main__":
    menu_principal()