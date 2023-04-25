from random import choice
from string import ascii_letters, digits, punctuation

"""
SPRINT DE ENTREGA:
Se solicita como entregable de este Sprint la implementación final de todos los conceptos vistos
durante el Módulo 1 de Python básico. Por tanto, se debe poner foco en lo siguiente:
● Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu
aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).
● Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
● Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe
cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
● Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
● Por cada cuenta debe pedir un número telefónico para contactarse.

● El programa no terminará de preguntar por los números hasta que todas las organizaciones
tengan un número de contacto asignado.
● El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
● Se debe guardar como un string.
A modo de entrega, se debe disponer un documento Word o PDF en el que se indique:
- Ruta del repositorio en GitHub

Consideraciones adicionales
- El código debe estar debidamente indentado
- El formato del documento Word queda a criterio del equipo.

"""

usuarios = [
    {"id": 1, "nombre": "Miguel Garay Gallardo",
        "teléfono": 98547621, "usuario": "", "contrasena": ""},
    {"id": 2, "nombre": "Franco Valdés Navarro",
        "teléfono": 36521478, "usuario": "", "contrasena": ""},
    {"id": 3, "nombre": "Viviana Vera Ceballos",
        "teléfono": 14785296, "usuario": "", "contrasena": ""},
    {"id": 4, "nombre": "Marcelo Lagos Perez",
        "teléfono": 36985214, "usuario": "", "contrasena": ""},
    {"id": 5, "nombre": "Olivia Norambuena Johnson",
        "teléfono": 36975214, "usuario": "", "contrasena": ""},
    {"id": 6, "nombre": "Francisco Sinatra Olivares",
        "teléfono": 36989814, "usuario": "", "contrasena": ""},
    {"id": 7, "nombre": "Orlando Borquez Diaz",
        "teléfono": 96985214, "usuario": "", "contrasena": ""},
    {"id": 8, "nombre": "Nicolás Ríos Gonzalez",
        "teléfono": 87985214, "usuario": "", "contrasena": ""},
    {"id": 9, "nombre": "Ivania Salas Sierra",
        "teléfono": 98521434, "usuario": "", "contrasena": ""},
    {"id": 10, "nombre": "Rosalia Garate López",
        "teléfono": 86985214, "usuario": "", "contrasena": ""}
]

# FUNCIONES

# Funcion de gestion y creacion de cuentas de usuario
# Franco: Cambié la función para que acepte la lista que desea ordenar y no esté definida dentro del alcance de la misma.


def gestion_usuario(lista_usuarios):
    # se avanza por la lista de usuarios
    for persona in lista_usuarios:
        # se toma el nombre completo
        parte1 = persona["nombre"]
        # se separa por los espacios
        palabras = parte1.split()
        # se crea una cadena vacia
        nueva_cadena = ""
        # se recorre esa cadena
        for p in palabras:
            # se toma la inicial y se une al id de usuario
            nueva_cadena = nueva_cadena + p[0] + str(persona["id"])
        # se almacena nombre de usuario en el diccionario que se encuentra en la lista
        persona["usuario"] = nueva_cadena
        print(persona["nombre"], "Su nueva cuenta de usuario es:", persona["usuario"])

def creador_contraseña():
    # Definir el número mínimo de caracteres:
    largo = 8

    # Definir el rango de letras para el generador de characteres

    letras_disponibles = ascii_letters + digits + punctuation

    # Hace un bucle en el que genera contraseñas y verifica si alguna cumple con los requisitos
    while True:

        # Crea la contraseña de 8 caracteres de una lista de carácteres
        contraseña = "".join(choice(letras_disponibles) for _ in range(largo))

        # Verifica que tenga al menos una mayúscula, una minúscula y un dígito
        if any(char.isupper() for char in contraseña) \
                and any(char.islower() for char in contraseña) \
                and any(char.isdigit() for char in contraseña):
            break

    # Devuelve la contraseña creada
    return contraseña

def asignador_contraseñas(lista_usuarios):
    # Itera sobre la lista de usuarios y les otorga una contraseña al llamar a la función creador_contraseña
    
    for persona in lista_usuarios:
        contraseña = creador_contraseña()
        persona.update({"contraseña":contraseña})

def impresion_lista(lista):
    for diccionario in lista:
        for key in diccionario:
            if key == "nombre":
                print(f"{key}: {diccionario[key]}")
            else:
                print(f"    {key}: {diccionario[key]}")

# EJECUCIÓN

# Agregando los nombres de usuarios
gestion_usuario(usuarios)

# Asignando contraseñas de manera aleatoria de acuerdo con los requerimientos
asignador_contraseñas(usuarios)

# Imprimiendo la información de la lista de usuarios con un formato agradable
impresion_lista(usuarios)