def mayor(a,b,c):
    if (a > b) and (a > c):
        print("El numero mayor es a: ",a)
    elif (b > a) and (b > c):
        print("El numero mayor es b: ",b)
    elif (c > a) and (c > b):
        print("El numero mayor es c: ",c)

x = int(input("Ingresa un numero a: "))
y = int(input("Ingresa un numero b: "))
z = int(input("Ingresa un numero c: "))

mayor(x,y,z)