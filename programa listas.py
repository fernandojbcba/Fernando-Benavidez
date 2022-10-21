lista=["fer","pablo","raul","tomas","marta",1,2,3,4,5,True, False]
print(lista)

meses=["enero","febrero","marzo","abril","mayo","junio"]
dias=["lunes","martes","miercoles","jueves","viernes"]
print (meses + dias)

estaciones=["invierno", "verano","otonio"]
print (estaciones)
estaciones.append("primavera")
print (estaciones)

estacion=estaciones.pop(0)
print (estacion)
print (estaciones)

estaciones.insert(0,"invierno")
print (estaciones)
estaciones.remove("invierno")
print(estaciones)

print("verano" in estaciones)
print("summer" in estaciones)
print(estaciones.index("otonio"))

estaciones.pop(-1)
print(estaciones)