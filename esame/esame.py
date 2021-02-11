from operator import itemgetter
file = open("glicemometers.txt", "r", encoding="cp1252")
max = 160
elenco = []
for line in file:
    lines = line.strip().split()
    if int(lines[2]) >= max:
        paziente = {"codice":lines[0], "orario":lines[1], "valore":lines[2]}
        elenco.append(paziente)
controllo = {}
for paziente in elenco:
    if paziente["codice"] not in controllo:
        controllo[paziente["codice"]] = 1
    else:
        controllo[paziente["codice"]] += 1
for paziente in elenco:
    for valore in controllo:
        if paziente["codice"] == valore:
            paziente["numero"] = controllo[valore]
elenco.sort(key=itemgetter("numero"), reverse = True)
for paziente in elenco:
    print(f"{paziente['codice']} {paziente['orario']} {paziente['valore']}")
