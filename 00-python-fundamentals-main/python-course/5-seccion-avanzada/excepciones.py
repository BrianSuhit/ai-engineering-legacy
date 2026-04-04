def suma_dos():
    while True: 
        a = input("numero 1: ")
        b = input("numero 2: ")
        try:
            resultado =  int(a) + int(b)
            break
        except:
            print("ingresa un numero, no texto")
        else:
            break
        finally: 
            print("esto se ejecuta siempre")
    return resultado


print(suma_dos())