file_incendio = open("incendio.txt", "r")
file_servizio = open("servizio.txt", "r")
file_riserva = open("riserva.txt", "r")
incendio = open("incendio2.txt", "w")
tabella = []
for line in file_incendio:
    lines = line.strip().split()
    riga = ""
    riga2 = ""
    for i in lines:
        riga2 += i
    for i in lines:
        riga = riga + " " + i
    tabella.append(list(riga2.strip()))
    incendio.write(riga.lstrip() + "\n")

listaServizio = []
listaRiserve = []

for line in file_servizio:
    lines = line.strip().split(";")
    dizSer = {"matricola":lines[0], "nome":lines[1], "grado":lines[2]}
    listaServizio.append(dizSer)

for line in file_riserva:
    lines = line.strip().split(";")
    dizRis = {"matricola":lines[0], "nome":lines[1], "grado":lines[2]}
    listaRiserve.append(dizRis)

for riga in range(8):
    for colonna in range(8):
        if tabella[riga][colonna] == 'f' and tabella[riga+1][colonna] == '.':
            tabella[riga+1][colonna] = "p"

pos = 0
for i in tabella:
    for j in i:
        if j == "p":
            pos += 1

primoTurno = {}
for lines in listaServizio:
    primoTurno[lines["matricola"]] = lines["grado"]
for lines in listaRiserve:
    primoTurno[lines["matricola"]] = lines["grado"]

chiavi = []

for key in primoTurno:
    chiavi.append(key)

for riga in range(8):
    for colonna in range(8):
        if tabella[riga][colonna] == 'p':
            tabella[riga][colonna] = chiavi[0]
            pompiere = chiavi[0]
            grado = int(primoTurno[chiavi[0]])
            for i in range(grado-1):
                indice = 0
                while riga >= 0:
                    if tabella[riga-1][colonna] == 'f':
                        tabella[riga-1][colonna] = '+'
                    indice += 1
                    riga -=1

            chiavi.pop(0)

indice=0
while indice<8:
    print(tabella[indice])
    indice=indice+1
