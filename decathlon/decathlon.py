def leggi_file(file):
    infile = open("risultati.csv", "r", encoding="utf-8")
    prima = infile.readline().rstrip().split(",")
    discipline = prima[1:11]
    tabella = []
    atl_max_disc = []
    max_disc = []
    for riga in infile:
        campi = riga.rstrip().split(",")
        risultati = []
        atleta = campi[0]
        for i in campi[1:11]:
            risultati.append(int(i))
        tabella.append(risultati)   #qui mi creo la tabella che uso poi dopo nella ricerda del
                                    #valore massimo per ogni disciplina


        massimo = max(risultati)
        indice = risultati.index(massimo)
        sottodiz = {"atleta":atleta,
                    "max":massimo,
                    "disciplina": discipline[indice]}
        atl_max_disc.append(sottodiz)

    #creazione della "funzione" che trova il valore massimo per ogni disciplina
    for i in range(0,len(tabella[0])):
        values = []
        for a in range(0,len(tabella)):
            values.append(tabella[a][i])

        migliore = max(values)
        sottodiz2 = {"disciplina":discipline[i],
                         "massimo":migliore}
        max_disc.append(sottodiz2)

    infile.close()
    return atl_max_disc,discipline,max_disc

def main():
    risultato = leggi_file("risultati.csv")
    atl_max_disc = risultato[0]
    discipline = risultato[1]
    max_disc = risultato[2]
    #print(discipline)
    #print(atl_max_disc)
    #print(max_disc)
    for i in atl_max_disc:
        for a in max_disc:
            if i["disciplina"]==a["disciplina"] and i["max"]==a["massimo"]:
                print(f"L'atleta {i['atleta']} ha fatto un super punteggio di {a['massimo']} punti nella disciplina: {a['disciplina']}")
main()
