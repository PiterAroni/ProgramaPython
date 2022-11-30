#SEMANA 3 Y SEMANA 4
print("------------------")
print("Bienvenido al menu")
print("------------------")
print("1.AREA DEL CIRCULO")
print("2.AREA DE UN TRIANGULO EQUILATERO")
opcion = int(input("Digite una opcion: "))
while opcion == 1 or opcion == 2:
    if opcion ==1:
        radio = float(input("Digite el valor del radio: "))
        areac = 3.14 * radio * radio
        print("El area del circulo es: ",areac)
    elif opcion ==2:
        lado = float(input("Digite el valor del lado: "))
        areat = (lado * lado * 1.73)/4
        print("El area del triangulo equilatero es: ",areat)
    else:
        print("OPCION NO VALIDA VUELVA A INTENTAR")
else:
    print("OPCION NO VALIDA VUELVA A INTENTAR")