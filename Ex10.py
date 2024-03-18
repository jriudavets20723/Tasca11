def dic(a, b):
    try:
        c = a/b
        print("La divisió de {} entre {} és {}".format(a, b, a/b))
    except ZeroDIvisionError:
        print("El segon parametre de la funcio no pot ser zero")

#Programa Principal
a = int(input("Introdueix el numerador: "))
b = int(input("Introdueix el denominador: "))
c = dic(a, b)