"Alcance global"
productos = []
ventas = []

def ingresar_productos():
    "Alcance local"
    menu_secundario = """
    Desea usted agregar un producto??
    (1) agregar
    (2) VOLVER
"""
    opcion = 0
    while opcion != 2 :
        print(menu_secundario)
        opcion = int(input("Seleccione una opcion "))
        if opcion == 1 :
            variable = 3
            nombre = input("Por favor ingrese el nombre del producto: ")
            cantidad = int(input("Por favor ingrese la cantidad de este producto: "))
            producto = {
                "nombre":nombre,
                "cantidad":cantidad
            }
            productos.append(producto)
    
def vender():
    opcion = 0
    menu_secundario = """
Bienvenido al subsistema de ventas
Que desea hacer?
   (1) Crear venta
   (2) Ver ventas
   (3) VOLVER
"""
    while opcion != 3:
        print(menu_secundario)
        opcion = int(input("Opcion seleccionada: "))
        if opcion == 1:
            ver_productos()
            producto = input("Seleccione el producto a vender: ")
            precio = float(input("Indique el precio: "))
            cantidad = int(input("Indique la cantidad: "))
            venta = {
                "producto": producto,
                "precio": precio,
                "cantidad": cantidad
            }
            ventas.append(venta)
        if opcion == 2:
            for venta in ventas:
                print(venta)

def ver_productos():
    for producto in productos:
        print(producto)

def menu_principal():
    bienvenida = """
    Bienvenido
       Al sistema de pulperia version 1.0
       Creador: Yo
       Menu de opciones
            (1) ingresar producto
            (2) ver productos
            (3) venta
            (4) SALIR
    """
    opcion = ""
    while opcion != "4":
        print(bienvenida)
        opcion = input("Opcion seleccionada: ")
        if opcion == "1":
            ingresar_productos()
        if opcion == "2":
            ver_productos()
        if opcion == "3":
            vender()
    
if __name__=="__main__":
    menu_principal()