nombre_persona = input("Ingrese un nombre: ")
edad_persona = int(input("Ingrese la edad: "))
edad_limite = 15

if edad_persona >= edad_limite:
    print("Puede entrar a la pelicula.")
else:
    print("No puede entrar.")
    
nota_persona = float(input("Ingrese la nota: "))

if nota_persona <= 70.0:
    print("Aplazado!")
else:
    print("Aprobado!")
    
if nombre_persona == "John":
    print("Hola John")
else:
    print("No eres John")
    
if nombre_persona != "John":
    print("No eres John")
else:
    print("Eres John")
    
activo = False
estado = input("Estado estudiante Activo (A) o Inactivo (I): ")
if estado == "A":
    activo = True
else:
    activo = False
    
if activo:
    print("El estudiante está activo")
else:
    print("El estudiante está inactivo")