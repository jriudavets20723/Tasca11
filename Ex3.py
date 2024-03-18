def filtrar(llista, c):
    f = list(filter(lambda x: x[0]==c.lower() or x[0]==c.upper(), llista))
    print("De la llista {}, les paraules que començen per {} són {}".format(llista, c, f))

#pp
llista = ["Josep", "Joana", "Jordi", "Maria", "Marc", "Pere", "Paula"]
c = "j"
filtrar(llista, c)