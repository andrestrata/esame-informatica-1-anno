from operator import itemgetter
file = open("20201214_QDV2020_001.csv", "r", encoding ="utf-8")
prima = file.readlines(1)
lista = []
for line in file:
    lines = line.strip().split(",")
    campi = {"nome provincia":lines[0][1:-1], "codice nuts 3 2021":lines[1][1:-1], "codice provincia storico":lines[2],
             "denominazione corrente":lines[3][1:-1], "valore":float(lines[4]), "indicatore":lines[5][1:-1],
             "unità di misura":lines[6][1:-1], "riferimento temporale":lines[7], "fonte originale":lines[8][1:-1]}
    lista.append(campi)
indicatori = []
for campi in lista:
    if campi["indicatore"] not in indicatori:
        indicatori.append(campi["indicatore"])
for i in range(0, len(indicatori)):
    print("{}. {}".format(i+1, indicatori[i]))
scelta = int(input("Inserire l'indice di un indicatore (1-90): "))
lista.sort(key = itemgetter("valore"), reverse = True)
print(f"Classifica secondo l'indicatore {indicatori[scelta-1]}:")
for campi in lista:
    if campi["indicatore"] == indicatori[scelta-1]:
        print("{}: {} {}".format(campi["denominazione corrente"], campi["valore"], campi["unità di misura"]))
