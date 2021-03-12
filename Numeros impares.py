def ejercicio1():
    num = 0
    impar = 0
    while num < 100:
        num = num + 1
        if num % 2:
            print(num)
            impar+=1
    print("total de impares" + str(impar))


def ejercicio2():
    letra = input("ingrese una letra")
    if letra == "s":
        print("la letra es valida:  " + str(letra))
    elif letra =="n":
        print("la letra ingresada es valida:  " + str(letra))
    else:
        print("la letra no es permitida")


#ejercicio1()
#ejercicio2()

def ejercicio10():

    numero= (int(input("Introduce un número entero")))
    numero2= (int(input('Introduce un segundo número entero')))
    totsum = numero+numero2
    totmul= numero*numero2
    print("la suma de los numeros es igual a:  " + str(totsum))
    print ("la multipilicacion de los numeros es igual a:  " + str(totmul))

#ejercicio10()

def ejercicio3():
 numero=(int(input("introduce un numero")))
 if numero % 2:
     print ("el numero es impar")
 else:
     print ("el numero es par")

#ejercicio3()

def ejercicio5():
   lista = [1,2,3,4,5,6,7,8,9,10]
   print("1." + str(lista))
   print("2." + str(lista))
   print("3." + str(lista))
   print("4." + str(lista))
   print("5." + str(lista))
   print("6." + str(lista))
   print("7." + str(lista))
   print("8." + str(lista))
   print("9." + str(lista))
   print("10." + str(lista))

#ejercicio5()

def ejercicio4():
    mayor = 0
    menor = 9999999999
    numeros = 5

    for i in range(numeros):
        num = int(input('Ingresa un número:'))
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num

    print(mayor)
    print(menor)

#ejercicio4()

def ejercicio6():
    num = int(input("Factorial de: "))
    f = 1
    for i in range(num+1):
        if i == 0:
            continue
        else:
            f = f * i

    print("resultado", str(f))

#ejercicio6()

def ejercicio8():
    num=int(input("ingrese un numero"))
    for i in range(1,11):
        print(num, " * ", num, " = ", num * i)
#ejercicio8()

def ejercicio7():
    num= int(input("ingrese un numero"))
    for n in range(2, num):
        if num % n == 0:
            print("No es primo")
            return False
    print("Es primo")
    return True
#ejercicio7()

import random
def ejercicio9():
    import random
    print("Ingrese cuantos numeros aleatorios desea obtener")
    n = int(input())
    aleatorios = [random.randint(0, 1000) for _ in range(n)]
    print(aleatorios)
ejercicio9()