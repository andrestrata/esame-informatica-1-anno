from operator import itemgetter

dizionario = {}
file = open("nazioni.txt", "r")
for line in file:
    line = line.strip().split()
    if line[3] == str(3):
        if line[2] not in dizionario:
            dizionario[line[2]] = 0.05
        elif line[2] in dizionario:
            dizionario[line[2]] += 0.05
    elif line[3] == str(2):
        if line[2] not in dizionario:
            dizionario[line[2]] = 0.1
        elif line[2] in dizionario:
            dizionario[line[2]] += 0.1
    elif line[3] == str(1):
        if line[2] not in dizionario:
            dizionario[line[2]] = 1
        elif line[2] in dizionario:
            dizionario[line[2]] += 1

lista_nazioni = []
for chiave in dizionario:
    nazioni = {"nazione": chiave, "medaglie equivalenti": dizionario[chiave]}
    lista_nazioni.append(nazioni)
# print(lista_nazioni)
print("medaglie d'oro equivalenti: ")
for chiave in dizionario:
    print(f"{chiave} {dizionario[chiave]:.2f}")

lista_nazioni.sort(key=itemgetter("medaglie equivalenti"), reverse=True)
print("le prime nazioni del medagliere sono: ")
ordinate = []
for nazioni in lista_nazioni:
    ordinate.append(nazioni["nazione"])
for i in range(0, 3):
    print(f"\t{i+1}) {ordinate[i]}")
