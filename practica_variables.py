'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
nombre = "Jorge"
print(type(nombre))
nombre = 1
print(type(nombre))
nombre = 9.5
print(type(nombre))
nombre = True
print(type(nombre))
nombre = False
print(type(nombre))
nombre = [1, 2, 3]
print(type(nombre))
nombre = {"ID":123}
print(type(nombre))

producto_grano = {
    "codigo":123,
    "nombre": "Granos",
    "activo": True
}
producto_lacteo = {
    "codigo":124,
    "nombre": "Lacteo",
    "activo": True
}
producto_pan = {
    "codigo":125,
    "nombre": "Pan",
    "activo": True
}
productos = [producto_grano, producto_lacteo, producto_pan]
print(productos)
horario = {
    "tipo":"Nocturno",
    "entrada": 7.30,
    "salida": 10.0
}
nota_fundamentos = {
    "asignatura":"Fundamentos de la progra",
    "profesor": "Jherom",
    "institucion": "CTP San Isidro",
    "horario":horario
}
nota_tics = {
    "asignatura":"TICs",
    "profesor": "Gabriel",
    "institucion": "CTP San Isidro",
    "horario":horario
}
print(nota_fundamentos)
print(nota_tics)