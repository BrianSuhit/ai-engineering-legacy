# MÁQUINA: Separador de Emails
# Input: Un email completo
def procesar_email(email):
    # Lógica (Los engranajes):
    # El método .split('@') corta el texto donde haya un @
    partes = email.split("@") 
    
    usuario = partes[0]  # Lo que está antes del @ (Brian.Suhit)
    dominio = partes[1]  # Lo que está después del @ (gmail.com)
    
    # Return: La máquina expulsa DOS cajas separadas
    return usuario, dominio

# USO (Desempaquetado):
# Pones las manos al final de la cinta y agarras las dos cajas
mi_usuario, mi_dominio = procesar_email("brian.suhit@gmail.com")

print(f"El usuario es: {mi_usuario}")
print(f"La empresa es: {mi_dominio}")