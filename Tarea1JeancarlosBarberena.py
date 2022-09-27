print("Le damos la bienvenida a la Calculadora Simple")

print("Ingrese el numero con la respectiva operacion que desea realizar")
opcion = int(input(" 1-Para Sumar\n 2-Para Restar \n 3-Para Multiplicar \n 4-Para Dividir \n 5-Para Número Primo \n 6-Para Número Palíndromo " ))      
if  opcion==1:
    primerDato = int(input("Ingrese el primer número"))
    segundoDato = int(input("Ingrese el segundo número"))
    resultado= primerDato+segundoDato
    resultado = str(resultado)
    print("¡El resultado de la suma fue procesado con éxito! El resultado es: "+ resultado)
    
    print("El programa se cerrará")
    exit()
    
if  opcion==2:
    primerDato = int(input("Ingrese el primer número"))
    segundoDato = int(input("Ingrese el segundo número"))
    resultado= primerDato-segundoDato
    resultado = str(resultado)
    print("¡El resultado de la resta fue procesado con éxito! El resultado es: "+ resultado)
    
    print("El programa se cerrará")
    exit()
    
if  opcion==3:
    primerDato = int(input("Ingrese el primer número"))
    segundoDato = int(input("Ingrese el segundo número"))
    resultado= primerDato*segundoDato
    resultado = str(resultado)
    print("¡El resultado de la multiplicación fue procesado con éxito! El resultado es: "+ resultado)
    
    print("El programa se cerrará")
    exit()
    
if  opcion==4:
    primerDato = float(input("Ingrese el primer número"))
    segundoDato = float(input("Ingrese el segundo número"))
    resultado= primerDato/segundoDato
    resultado = str(resultado)
    print("¡El resultado de la división fue procesado con éxito! El resultado es: "+ resultado)
    
    print("El programa se cerrará")
    exit()
    
if opcion==5:
    variableAux=0 #Esta variable se utiliza para verifiar el condicional, si es 1 el número ingresado es primo
                  #Si es 0, el número no es primo
    primerDato= int(input("Ingrese un número"))
    if primerDato>1:
        for i in range(2,primerDato):
            resto=primerDato%i
            if resto==0:
                variableAux+=1
        if variableAux==0:
            print("Es primo")
        else:
            print("No es primo")
    print("El programa se cerrará")
    exit()        

if opcion==6:
   primerDato= int(input("Ingrese un número"))
   palindromo = str(primerDato) == str(primerDato)[::-1]
   print ("¿El número es palíndromo? " + str(palindromo)) 
exit()
