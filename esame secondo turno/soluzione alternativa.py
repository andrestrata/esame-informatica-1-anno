def leggiFile(Diz,file):
    infile = open(file, "r")
    for str in infile:
        str = str.strip().split()
        list = []
        list.append(str[1])
        if str[0] in Diz:
            Diz[str[0]].append(str[1])
        else:
            Diz[str[0]] = list
    infile.close()
    return Diz

def Trova_sosp(Prod, Acq, sosp):
    for prod in Prod:
        if Prod[prod] != Acq[prod]:
            sosp.append(prod)
    return sosp

def sosp(Prod, Acq, sosp):
    print("Elenco transizioni sospette")
    print()
    for prod in sosp:
        print("Codice prodotto: %s" %(prod))
        print("Rivenditore ufficiale: %s" %(Prod[prod][0]))
        print("Lista Rivenditori: " , end="")
        for i in range (len(Acq[prod])):
            print("%s " %(Acq[prod][i]), end="")
        print("\n")
    return

Prodotti = {}
Acquisti = {}
sospetti = []
Prodotti = leggiFile(Prodotti, "prodotti.txt")
Acquisti = leggiFile(Acquisti, "acquisti.txt")
Trova_sosp(Prodotti, Acquisti, sospetti)
sosp(Prodotti, Acquisti, sospetti)
