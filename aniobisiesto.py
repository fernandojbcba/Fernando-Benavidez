anio = int (input("ingresse el años para saber si es bisiesto :"))

if anio % 400 == 0 or (anio % 100 != 0 and anio % 4 == 0):
    print ("el año ", anio, "es bisiesto" )
else:    
    print ("el años ", anio, "no es bisiesto" )