
"""Pedir usuario y contrasenia"""
def usuario_y_contrasena ():
    for i in range (3):
        usuario = input ("ingrese su usario: ")
        contra = input ("ingrese su contrana: ")
        if usuario == "user" and contra == "1234":
            return True
        else:
            print (f"usurio y contrasenia incorrecta, le quedan {2-i} oportunidades")
    return False
