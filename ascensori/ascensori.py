def spostamenti(ascensore, partenza, arrivo):
    movimenti = abs(ascensore["piano"] - partenza) + abs(partenza - arrivo)
    ascensore["piano"] = arrivo
    ascensore["movimenti"] += movimenti
WATT = 100
file = open("movimenti.txt", "r")
normale = {"piano": 0, "movimenti": 0}
risparmio = {"piano": 0, "movimenti": 0}
for line in file:
    lines = line.strip().split()
    partenza = int(lines[0])
    arrivo = int(lines[1])

    spostamenti(normale, partenza, arrivo)
    if arrivo > partenza:
        spostamenti(risparmio, partenza, arrivo)
print("ascensore senza risparmio")
print("Ascensore senza risparmio")
print("Spostamenti:", normale["movimenti"], "Consumo:", normale["movimenti"]*WATT, "W")
print("Ascensore con risparmio")
print("Spostamenti:", risparmio["movimenti"], "Consumo:", risparmio["movimenti"]*WATT, "W")

risparmioAssoluto = normale["movimenti"] - risparmio["movimenti"]
risparmioRelativo = risparmioAssoluto / normale["movimenti"] * 100.0
