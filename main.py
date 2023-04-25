from random import choice
from string import ascii_letters, digits, punctuation

usuarios = [
        {"id":1,"nombre":"Miguel Garay Gallardo","telefono":98547621},
        {"id":2,"nombre":"Franco Valdés Navarro", "telefono":36521478},
        {"id":3,"nombre":"Viviana Vera Ceballos", "telefono":14785296},
        {"id":4,"nombre":"Marcelo Fuentes Oliva", "telefono":36985214},
]

def validacion():
    """
    Funcion para validar que las opciones digitadas sean correctas
    """
    global opc_disponible
    opcion_ingresada = input()
    while True:
        if opcion_ingresada in opc_disponible:
            return opcion_ingresada 
        else:
            print("Opcion Ingresada no valida")
            opcion_ingresada = input()


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