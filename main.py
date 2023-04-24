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