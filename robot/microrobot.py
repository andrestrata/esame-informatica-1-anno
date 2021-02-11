def creaTab():
    tab = []
    while len(tab) < 5:
        lista = []
        while len(lista) < 5:
            lista.append(0)
        tab.append(lista)
    return tab
def cM(lines3):
    lista = []
    riga = list(lines3)
    while len(riga) > 0:
        lista.append(riga[0]+riga[1])
        riga.pop(0)
        riga.pop(0)
    return lista
def moves(riga, colonna, listaMovimenti):
    percorso = []
    percorso.append([riga, colonna])
    for i in listaMovimenti:
        if i == "+v":
            riga += 1
            percorso.append([riga, colonna])
        elif i == "-v":
            riga -= 1
            percorso.append([riga, colonna])
        elif i == "+o":
            colonna += 1
            percorso.append([riga, colonna])
        elif i == "-o":
            colonna -= 1
            percorso.append([riga, colonna])
    return percorso
dizionario = []
file = open("traiettorie.txt", "r", encoding ="cp1252")
for line in file:
    lines = line.strip().split()
    dati = {"nome":lines[0], "partenza":[int(lines[1])-1, int(lines[2])-1],
    "movimenti":cM(lines[3])}
    dizionario.append(dati)
print(dizionario)
file.close()
spostamenti = {}
for dati in dizionario:
    spostamenti[dati["nome"]] = (moves(dati["partenza"][0], dati["partenza"][1], dati["movimenti"]))
print(spostamenti)
caselle = 0
for i in spostamenti["Ra9012"]:
    if i in spostamenti["Rj6k"]:
        caselle += 1
print(f"ci sono {caselle} caselle visitate da entrambi i robot Ra9012 e Rjk6")
