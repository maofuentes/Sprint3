from random import choice
from string import ascii_letters, digits, punctuation

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