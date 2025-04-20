def leap_year():
    year = int(input("Ingrese un año: "))
    resultado = "bisiesto" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "no bisiesto"
    print(f'El año {year} es {resultado}')
