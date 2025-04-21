def es_bisiesto(year):

  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False
year_ingresado = int(input("Ingrese un año: "))
if es_bisiesto(year_ingresado):
  print(f"El año {year_ingresado} es bisiesto")
else:
  print(f"El año {year_ingresado} no es bisiesto")
