def StringtoList(c):
    r = [x for x in c]
    print("De la cadena {} hem creat la llista {}".format(c, r))

#ProgramaPrincipal

c = input("Introdueix una paraula: ")
StringtoList(c)