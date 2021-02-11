from operator import itemgetter

serieA = open("serieA.txt", "r")
filtri = open("filtri.txt", "r")

listaGiocatori = []
listaFiltri = []

for line in serieA:
    lines = line.split()
    giocatore = {"cognome": lines[0], "nome": lines[1], "presenze": lines[2], "media": lines[3], "squadra": lines[4]}
    listaGiocatori.append(giocatore)
# print(listaGiocatori)
for line in filtri:
    lines = line.split()
    giocatore = {"cognome": lines[0], "nome": lines[1]}
    listaFiltri.append(giocatore)
# print(listaFiltri)
for i in listaFiltri:
    for j in listaGiocatori:
        if i["cognome"] == j["cognome"]:
            listaGiocatori.remove(j)
# print(listaGiocatori)

for i in listaGiocatori:
    print(i["cognome"], i["nome"], i["presenze"], i["media"], i["squadra"])

listaGiocatori.sort(key=itemgetter("presenze"))

print(f"presenze min: {listaGiocatori[0]['presenze']} {listaGiocatori[0]['cognome']} {listaGiocatori[0]['nome']}")
print(f"presenze min: {listaGiocatori[-1]['presenze']} {listaGiocatori[-1]['cognome']} {listaGiocatori[-1]['nome']}")
