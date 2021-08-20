opcion = 1
while opcion < 3:
    print("""
        Bienvenido al sistema
        Opciones disponibles
        (1) Saludar
        (2) Ver patata
        (3) TERMINAR
    """)
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        print("Hola")
    elif opcion == 2:
        print("patata")