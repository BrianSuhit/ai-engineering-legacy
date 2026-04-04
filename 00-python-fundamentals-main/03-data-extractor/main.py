import re

with open("03-data-extractor/datos_sucios.txt") as archivo:
    contenido_del_archivo = archivo.read()
    
print("-" * 30)
print("Iniciando escaneo de emails...")

patron_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# 2. Escanear (Find All)
# Sintaxis: re.findall(MOLDE, DONDE_BUSCAR)
emails_encontrados = re.findall(patron_email, contenido_del_archivo)

print(f"Se encontraron {len(emails_encontrados)} emails:")
for email in emails_encontrados:
    print(f"  -> {email}")
    
print("-" * 30)
print("Iniciando escaneo de teléfonos...")

patron_telefono = r"[\+\(]?\d+[\d \-\(\)]+"

telefonos_encontrados = re.findall(patron_telefono, contenido_del_archivo)

telefonos_reales = [tel for tel in telefonos_encontrados if len(tel) >= 8]

print(f"Se encontraron {len(telefonos_reales)} teléfonos:")
for tel in telefonos_reales:
    print(f"  -> {tel.strip()}") # .strip() quita espacios sobrantes al principio o final