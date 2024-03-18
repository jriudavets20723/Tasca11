def imprimir_fitxer(m):
    a = []
    with open (m, "r") as f:
        for e in f:
            c = e.split("\n")
            a.append(c[0])
    print(a)

def afegir_fitxer(m, llista):
    with open(m, "a+") as f:
        for e in llista:
            f.write(e+ "\n")

#Programa Principal
fitxer = "/home/cicles/Documentos/ex11.txt"
llista = ["Fede", "Hugo", "Ian", "Jordi", "Oscar"]
imprimir_fitxer(fitxer)
afegir_fitxer(fitxer, llista)
