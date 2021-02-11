from operator import itemgetter
file = open('glicemometers.txt', 'r')
elenco = []
for line in file:
    lines = line.strip().split()
    if int(lines[2]) >= 200:
        paziente = {'codice':lines[0], 'orario':lines[1], 'valore':lines[2]}
        elenco.append(paziente)
controllo = {}
i = 1
for paziente in elenco:
    if paziente['codice'] not in controllo:
        controllo[paziente['codice']] = i
    else:
        controllo[paziente['codice']] += 1
print(controllo)
for codice in controllo:
    for paziente in elenco:
        if codice == paziente['codice']:
            paziente['numero'] = controllo[codice]
print(elenco)
elenco.sort(key=itemgetter('numero'), reverse=True)
for paziente in elenco:
    print(f"{paziente['codice']}\t{paziente['orario']}\t{paziente['valore']}")
