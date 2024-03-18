import os

companys = ["Fede", "Pepe", "Jordi", "Ian", "Hugo", "Alvaro", "Leiner", "Sergi", "Joanr", "ayoub", "Pisha", "Anas", "David", "Sebas"]
os.mkdir("/home/cicles/ao/Python/prova")
os.chdir("/home/cicles/ao/Python/prova")
with open("ex12.txt", "w") as f:
    print("Fitxer creat correctament!")
    for e in companys:
        f.write(e+"\n")
professors = ["David", "Pep", "Fela", "Lluís", "Joan"]
with open("ex12.txt", "a+") as f:
    for e in professors:
        f.write(e+"\n")
a = []
with open("ex12.txt", "r") as f:
    for e in f:
        c = e.split("\n")
        a.append(c[0])
print(a)