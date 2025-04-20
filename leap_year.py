def es_bisiesto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
ano = int(input("Ingrese un año: "))
if es_bisiesto(ano):
    print(f"El año {ano} es bisiesto")
else:
    print(f"El año {ano} no es bisiesto")
