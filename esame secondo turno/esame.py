fileProdotti = open("prodotti.txt", "r")
fileAcquisti = open("acquisti.txt", "r")
listaProdotti = {}
listaAcquisti = {}
for line in fileProdotti:
    lines = line.strip().split()
    if lines[0] not in listaProdotti:
        listaProdotti[lines[0]] = [lines[1]]
    else:
        listaProdotti[lines[0]].append(lines[1])
for line in fileAcquisti:
    lines = line.strip().split()
    if lines[0] not in listaAcquisti:
        listaAcquisti[lines[0]] = [lines[1]]
    else:
        listaAcquisti[lines[0]].append(lines[1])
lista_sospetti = {}

for i in listaProdotti:
    for j in listaAcquisti:
        if i == j:
            if listaProdotti[i] != listaAcquisti[j]:
                lista_sospetti[j] = listaAcquisti[j]

print("elenco transazioni sospette")
print()
for codice in lista_sospetti:
    print(f"codice prodotto: {codice}\n"
          f"rivenditore ufficiale: {listaProdotti[codice]}\n"
          f"lista rivenditori: {lista_sospetti[codice]}")
    print()
