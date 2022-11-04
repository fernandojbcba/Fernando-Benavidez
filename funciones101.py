###########################################################################
# #funciones
###########################################################################


# Las funciones en Python, y en cualquier lenguaje de programación, son estructuras esenciales de código. Una función es un grupo de instrucciones que constituyen una unidad lógica del programa y resuelven un problema muy concreto.


###########################################################################
# #funciones sin parametros
###########################################################################

# def mifuncion():
#     print("hola mundo")
#     print("estoy en el curso de codo a codo")

# mifuncion()
# mifuncion()
# mifuncion()


#### mostrar la importancia no son mas pasos?
#### no es mas facil lanzar solo el print?

# print("hola mundo")
# print("hola mundo")
# print("hola mundo")


#############################################################################################
# solo son 3 lineas en este ejemplo claramente no se puede ver la diferencia
# imagenemos que tenemos que calcular la cantidad de alumnos que aprobaron con mas de 7
#############################################################################################

# def aprobados():
#     a= int(0)
#     d= int(0)
#     while str(input("ingrese fin para terminar: ")) != "fin":
#         nota = int(input("ingresa tu nota: "))
#         if nota >= 7 and nota <= 10:
#             print("has aprobado")
#             a=a+1
#             print("cantidad de aprobados: ", a)
#         elif nota <= 0 or nota >= 10:
#             print("has ingresado un valor incorrecto")
#         else:
#             print("has desaprobado")
#             d=d+1
#             print("la cantidad de desaprobados es : ", d)

# aprobados()


######################################################################################
# crear un programa que permita almacenar los costos mensuales de una persona
######################################################################################

# def gastos():
#     sueldo = int(input("ingresa tu sueldo en pesos: $"))
#     gastosfinales = int(0)
#     while str(input("ingrese fin para terminar: ")) != "fin":
#         gasto = int(input("ingresa tus gastos en pesos: $"))
#         if gastosfinales < sueldo:
#             gastosfinales= gastosfinales + gasto
#             print("tus gastos hasta el momento son: $", gastosfinales)
#             print("tu saldo actual es: $", sueldo - gastosfinales)
#         else:
#             print("no tienes más plata!!!")

# gastos()


###########################################################################
# Determinar si un año es bisiesto
###########################################################################

# def bisiesto():
#     while str(input("ingrese fin para terminar: ")) != "fin":
#         año= int(input("ingresa el año que quieras para determinar si es bisiesto: "))
#         resto = año % 4
#         if resto == 0:
#             print("es un año bisiesto")
#         else:
#             print("no es año bisiesto")

# bisiesto()

###########################################################################
# crear un programa para Loggearse en una web
###########################################################################
# def loggeo():
#     print(" ####################################### \n Registrate y completa tus datos \n #######################################"  )
#     userReg = input("ingrese un usuario : ")
#     passwordReg = input("ingrese una contraseña : ")
#     print("\n     gracias por registrarte!! ☺")
#     ### log in ###
#     print(" ####################################### \n Para ingresar al sitio debe loggearse \n #######################################")
#     if userReg == input("ingrese su usuario : ") and passwordReg == input("ingrese su password : "):
#         print("Bienvenido!!")
#     else:
#         print("Usuario y/o contraseña incorrecta!!")

# loggeo()



###########################################################################
# # piedra papel o tijera
###########################################################################

# def juego1():
#     print("###################################")
#     print("juguemos a piedra, papel o tijera")
#     print("###################################")
#     print("\n ingresa 1 para piedra \n ingresa 2 para papel \n ingresa 3 para tijera \n ")
#     print("###################################")

#     piedra = int(1)
#     papel = int(2)
#     tijera = int(3)

#     while str(input("ingrese fin para terminar: ")) != "fin":
    
#         usuario1 = int(input("Turno jugador 1 \n ingresa \n 1 para piedra \n 2 para papel \n 3 para tijera: \n"))
#         usuario2 = int(input("Turno jugador 2 \n ingresa \n 1 para piedra \n 2 para papel \n 3 para tijera: \n"))
        
#         if usuario1 == 1 and usuario2 == 3 :
#             print("##########################")
#             print("usuario 1 gana")
#             print("piedra le gana a tijera")
#             print("##########################")
#         elif usuario1 == 2 and usuario2 == 1:
#             print("##########################")
#             print("usuario 1 gana")
#             print("papel le gana a piedra")
#             print("##########################")
#         elif usuario1 == 3 and usuario2 == 2:
#             print("##########################")
#             print("usuario 1 gana")
#             print("tijera le gana a papel")
#             print("##########################")
#         elif usuario1 == 1 and usuario2 == 2:
#             print("##########################")
#             print("usuario 2 gana")
#             print("papel le gana a piedra")
#             print("##########################")
#         elif usuario1 == 2 and usuario2 == 3:
#             print("##########################")
#             print("usuario 2 gana")
#             print("tijera le gana a papel")
#             print("##########################")
#         elif usuario1 == 3 and usuario2 == 1:
#             print("##########################")
#             print("usuario 2 gana")
#             print("piedra le gana a tijera")
#             print("##########################")
#         elif usuario1 > 3 or usuario2 > 3:
#             print("##########################")
#             print("El numero ingresado es incorrecto")
#             print("##########################")
#         elif usuario1 <= 0 or usuario2 <= 0:
#             print("##########################")
#             print("El numero ingresado es incorrecto")
#             print("##########################")
#         else:
#             print("##########################")
#             print("empate")
#             print("##########################")

# juego1()


###########################################################################
# Simular cajero
###########################################################################




# def cajero():
#     print("Hola Bienvenido al cajero de codo a codo")
#     idioma = int(input("ingresa \n 1 para elegir el idioma en español \n 2 para ingles \n 3 para portugues: "))
#     if idioma == 1:
#         print("has seleccionado el idioma español")
#         print("ingresa tu clave para acceder a tu cuenta \n la clave es 1234 ")
#         clave = int(input("ingresa tu clave: "))
#         nombre = str(input("ingresa tu nombre: "))
#         saldo = float(85200)
#         saldoDolar = float(0)
#         if clave == 1234:
#             print("#########################################")
#             print("Bienvenido a tu cuenta", nombre, "!!")
#             print("#########################################")
#             print("seleciona una opcion y presiona lo siguiente: ")
#             print("#########################################")
#             print("     #1  consultar saldo")
#             print("     #2  depositar dinero")
#             print("     #3  extraer dinero")
#             print("     #4  transferir dinero")
#             print("     #5  comprar dolares")
#             print("     #6  vender dolares")
#             print("     #7  crear plazo fijo")
#             print("     #8  ver ultimos movimientos")
#             print("     #9  salir de la cuenta")
#             print("#########################################")
#             opcion = int(input("ingresa tu opcion: "))
#             #1consultar saldo
#             if opcion == 1:
#                 print("tu saldo actual en pesos es de: $" ,saldo)
#             #2depositar dinero
#             elif opcion == 2:
#                 print("#########################################")
#                 ingreso = int(input("digite por teclado el monto de su dinero a ingresar y luego inserte su dinero: "))
#                 print("#########################################")
#                 saldoActual = saldo + ingreso
#                 print("--Gracias por ingresar su dinero, su saldo actual es de: $",saldoActual, "--")
#             #3extraer dinero
#             elif opcion == 3:
#                 extraccion = int(input("ingresa el monto a extraer: "))
#                 saldoActual = saldo - extraccion
#                 print("gracias por extraer, tu saldo restante es: $" , saldoActual)
#             #4transferir dinero
#             elif opcion == 4:
#                 tranferir = int(input("ingrese el cbu de la cuenta a la cual deseas tranferir: "))
#                 monto = int(input("ingresa el monto a tranferir: "))
#                 print("#########################################################")
#                 print("Estas por realizar una transferencia al numero de cuenta ", tranferir , "con el siguiente monto: ", monto, "estas seguro que deseas realizar esta accion ?")
#                 print("#########################################################")
#                 saldoActual = saldo - monto
#                 confirmar = str(input("ingresa: \n     # si para confirmar la transferencia. \n     # no para cancelar: \n "))
#                 if confirmar == "si":
#                     print("gracias tu tranferencia ha sido realizada!, tu saldo actual es de: $" , saldoActual )
#                 elif confirmar == "no":
#                     print("has cancelado tu transferencia")
#                 else:
#                     print("has ingresado un valor invalido")
#             #5comprar dolares
#             elif opcion == 5:
#                 print("#####################################")
#                 print("    el precio del dolar es de $160")
#                 print("    tu saldo es el siguiente: " , saldo)
#                 print("#####################################")
#                 compraDolar = float(input("ingresa el monto de dolares a comprar: "))
#                 print("#####################################")
#                 print("estas seguro de comprar : u$s" , compraDolar, " dolares ?")
#                 confirma  = str(input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
#                 print("#####################################")
#                 if confirma == "si":
#                     conversion = compraDolar * 160
#                     saldoActual = saldo - conversion
#                     saldoDolar = saldoDolar + compraDolar
#                     print("#####################################################")
#                     print("tu saldo en tu cuenta pesos es de: $" , saldoActual)
#                     print("tu saldo en tu cuenta dolares es de: u$s" , saldoDolar )
#                     print("#####################################################")
#                 elif confirma == "no":
#                     print("has cancelado tu compra")            
#             #6vender dolares


#             #7crear plazo fijo
            
#             #8ver ultimos movimientos
#             #9salir de la cuenta
#         else:
#             print("clave incorrecta")
#     elif idioma == 2:
#         print("has seleccionado ingles")
#     elif idioma == 3:
#         print("has seleccionado portugues")
#     else:
#         print("opcion incorrecta")
# cajero()









###########################################################################
# #funciones con parametros - sumar
###########################################################################

# def suma(num1, num2):
#     print("tu suma es la siguiente:", num1 + num2)
    
# suma(10,20)

# suma(101,20)



###########################################################################
# #funciones con parametros - resta
###########################################################################

# def resta(num1, num2):
#     print(num1 - num2)

# resta(10,20)

# resta(101,20)


###########################################################################
# #funciones con parametros - multiplicar
###########################################################################

# def multiplicar(num1, num2):
#     print(num1 * num2)

# multiplicar(10,20)

# multiplicar(101,20)


###########################################################################
# #funciones con parametros dividir
###########################################################################

# def dividir(num1, num2):
#     print(num1 / num2)

# dividir(10,20)

# dividir(101,20)


# dividir(int(input("ingresa el num1 :")),int(input("ingresa el num2 :")))


###########################################################################
## tarea realizar esta funcion pero con una division entera
###########################################################################


#############################################################################################
## tarea a la misma division agregarle la posibilidad de ingresar los valores por teclado
#############################################################################################



###########################################################################
# #funciones con parametros - saludar - solo ingreso de nombre
###########################################################################

# def saludar(nombre):
#     print("hola", nombre , "gracias por cursar en codo a codo")

# saludar("Emanuel")
# saludar("Carlos")
# saludar("Maria")

# saludar(input("ingresa tu nombre: "))


###########################################################################
# #funciones con parametros - saludar 2 - ingreso de nombre y apellido
###########################################################################

# def saludar(nombre, apellido):
#     print("hola", nombre, apellido , "gracias por cursar en codo a codo")


# saludar(input("ingresa tu nombre: "), input("ingresa tu apellido: "))


##############################################################################
# #funciones con parametros - saludar 3 - ingreso de nombre, apellido y edad
##############################################################################

# def saludar(nombre, edad):
#     if edad >= 18:
#         print("hola", nombre, "puedes cursar en codo a codo, ya que tienes ", edad ,  "años")
#     else:
#         print("hola", nombre, "no puedes cursar en codo a codo, ya que tienes ", edad ,  "años")

# saludar(input("ingresa tu nombre: "), int(input("ingresa tu edad: ")))


##############################################################################
# #funciones con parametros - mensaje diario con tuplas
##############################################################################

# tuplasemana = ("domingo","lunes", "martes", "miercoles", "jueves", "viernes", "sabado")
# def mensajediario(dia):
#     if dia == tuplasemana[0]:
#         print("hoy es:", tuplasemana[0], "excelente dia para aprender python" )
#     elif dia == tuplasemana[1]:
#         print("hoy es:", tuplasemana[1], "excelente dia para aprender python" )
#     elif dia == tuplasemana[2]:
#         print("hoy es:", tuplasemana[2], "excelente dia para aprender python" )
#     elif dia == tuplasemana[3]:
#         print("hoy es:", tuplasemana[3], "excelente dia para aprender python" )
#     elif dia == tuplasemana[4]:
#         print("hoy es:", tuplasemana[4], "excelente dia para aprender python" )
#     elif dia == tuplasemana[5]:
#         print("hoy es:", tuplasemana[5], "excelente dia para aprender python" )
#     elif dia == tuplasemana[6]:
#         print("hoy es:", tuplasemana[6], "excelente dia para aprender python" )
#     else:
#         print("es otro dia")

# mensajediario("lunes")
# mensajediario(tuplasemana[3])
# mensajediario(input("escribe tu dia: "))

###########################################################################
# #funciones con parametros calcular el IMC
###########################################################################

# def imc(peso, altura):
#     indice = peso / (altura * altura)
#     print(indice)

#     if indice <16.00:
#         print("Infrapeso: Delgadez Severa")
#     elif indice > 16.00 and indice <16.99:
#         print("Infrapeso: Delgadez moderada")
#     elif indice > 17.00 and indice <18.49:
#         print("Infrapeso: Delgadez aceptable")
#     elif indice > 18.50 and indice <24.99:
#         print("peso normal")
#     elif indice > 25.00 and indice <29.99:
#         print("sobrepeso")
#     elif indice > 30.00 and indice <34.99:
#         print("Obeso: Tipo I")
#     elif indice > 35.00 and indice <39.99:
#         print("Obeso: Tipo II")
#     elif indice > 40.00:
#         print("Obeso: Tipo III")
#     else:
#         print("algo salio mal")

# imc(float(input("ingresa tu peso en kg: ")), float(input("ingresa tu altura en metros: ")))


###########################################################################
# #funciones con parametros calcular el IVA
###########################################################################

# def impuesto(iva, producto):
#     print("el precio del producto sin iva es: ", producto)
#     soloiva = (producto * iva)/100
#     print("el iva del producto es: ", soloiva)
#     productoiva = soloiva + producto
#     print("el precio del prducto con iva: ", productoiva)

# # impuesto(21,15000)
# impuesto(float(input("ingrese el iva: ")), float(input("ingrese el valor del producto: ")))


###########################################################################
# #funciones con parametros -semaforo
###########################################################################
# def semaforo(color):

#     if color == "1":
#         print("Circule!")
#     elif color == "2":
#         print("Precaucion!")
#     elif color == "3":
#         print("Detenerse!")
#     else:
#         print("valor invalido")

# semaforo(input("ingrese color de semaforo (1 - verde / 2 - Amarillo / 3 -Rojo): "))




###########################################################################
# #funciones con parametros y return
###########################################################################
###########################################################################
## print() es una de las funciones incorporadas del lenguaje. Como toda función, puede recibir determinados argumentos (particularmente print() acepta cualquier cantidad de argumentos) y tener un resultado. En cambio, return es una palabra reservada, que opcionalmente puede estar sucedida de una expresión o una variable. Pero lo fundamental es que cumplen objetivos totalmente distintos. print() sirve para mostrar un mensaje en la pantalla de una aplicación de consola, mientras que return se utiliza para establecer el resultado (o valor de retorno) de una función. Así, return es una operación mucho más genérica que print(), aunque solo puede usarse dentro de las funciones: no puede haber un return en cualquier otro lugar del código que no sea el interior de una función. print() solo puede usarse, naturalmente, en aplicaciones de consola, pues sirve únicamente para mostrar un mensaje en la consola
###########################################################################
## mostrar resultado de multiplicar
###########################################################################

# def multiplicar(num1 , num2):
#     mul = num1 * num2
#     return print("el resultado de mi multiplicacion es la siguiente:",mul)
#     # return mul

# multiplicar(20, 2)


###########################################################################
## tarea realizar la misma funcion pero con suma, resta y division
###########################################################################

###########################################################################
## tarea ahora agregar la posibilidad de ingresarlo por teclado
###########################################################################



###########################################################################
## el menor y mayor de dos numeros
###########################################################################

# def maximo(a,b):
#     if x>y:
#         return x, print("x es mayor que y")
#     else:
#         return y, print("y es mayor que x")


# def minimo(a,b):
#     if x<y:
#         return x, print("x es menor que y")
#     else:
#         return y, print("y es menor que x")

# #--------------------------
# x=int(input("El número x: "))
# y=int(input("El número y: "))

# maximo(x,y)
# minimo(x,y)


##########################################################


########################################################################################
## tarea realizar una funcion donde podamos determinar cual es el mayor de 3 numeros
########################################################################################


########################################################################################
## tarea realizar una funcion donde permita realizar una calculadora
## con las 4 operaciones fundamentales suma, resta, division , multiplicacion   
########################################################################################


# ######################################
# contando el largo de un string
# ######################################

# cadena = "hola chicos estoy cursando"
# print(len(cadena))