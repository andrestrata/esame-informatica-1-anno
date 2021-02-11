from random import shuffle


def risultatoMano(carta1, carta2):
    if carta1 == carta2:  # se le carte sono uguali
        return "pareggio"
    elif carta1 == "rosso" and carta2 != "rosso":  # se la prima carta è rossa e la seconda non rossa
        return "vince giocatore 1"  # essendo la più alta vince su tutte
    elif carta1 == "giallo" and carta2 != "giallo":  # se la prima carta è gialla e la seconda non gialla
        return "vince giocatore 2"  # vince il giocatore 2 perché la gialla perde da tutte
    elif carta1 == "verde":  # se la prima carta è verde
        if carta2 == "rosso":  # se la seconda è rossa
            return "vince giocatore 2"  # vince il 2
        elif carta2 == "giallo":  # se la seconda è gialla
            return "vince giocatore 1"  # vince l'1


def punteggio_mano(carta1, carta2):  # rosso 5 verde 3 giallo 1
    if carta1 != carta2:  # se le carte sono diverse
        if carta1 == "rosso" and carta2 != "rosso":  # se la prima è rossa e la seconda non rossa
            if carta2 == "verde":  # se la seconda è verde
                return 8
            elif carta2 == "giallo":  # se la seconda è gialla
                return 6
        else:  # se la prima è verde e la seconda è gialla
            return 4
    if carta1 == carta2:  # se le carte sono uguali
        if carta1 == "rosso":  # se sono due rosse
            return 10
        elif carta1 == "verde":  # se sono due verdi
            return 6
        elif carta1 == "giallo":  # se sono due gialle
            return 2


infile = open("mazzo.txt", "r")  # apertura file
mazzo = []  # mazzo vuoto
for carta in infile:  # iterazione delle righe
    carta = carta.strip().lower()  # pulisce le righe
    mazzo.append(carta)  # le aggiunge al mazzo vuoto
infile.close()  # chiusura file
shuffle(mazzo)  # mischia il mazzo
# distribuzione carte
carte_giocatore1 = []  # lista vuota carte del primo giocatore
carte_giocatore2 = []  # lista vuota carte del secondo giocatore
for i in range(0, len(mazzo)):  # iterazione mazzo completo
    if i % 2 == 0:
        carte_giocatore1.append(mazzo[i])  # carte a indice pari al giocatore 1
    else:
        carte_giocatore2.append(mazzo[i])  # carte indice dispari al giocatore 2
# inizio del gioco
punteggioG1 = 0  # inizializza i punteggi
punteggioG2 = 0
inizio_mano = input("premere INVIO: ")  # premere "invio" per far iniziare la mano
n = 0  # indicizza la mano
punteggioPareggio = {}  # dizionario vuoto per tracciare i punteggi
punteggioPareggio["X"] = 0  # assegna alla chiave "X" il valore 0, mi serve per tenere il punteggio dei pareggi
while inizio_mano == "" and n <= 14:  # inizio ciclo while finché n è minore di 15 (fine carte)
    print(f"mano n.{n + 1}")  # stampa mano
    carta_giocatore1 = carte_giocatore1[n]  # carta del primo giocatore
    carta_giocatore2 = carte_giocatore2[n]  # carta secondo giocatore
    print(f"carta G1: {carta_giocatore1}")  # stampa a video le carte
    print(f"carta G2: {carta_giocatore2}")
    risultato = risultatoMano(carta_giocatore1, carta_giocatore2)  # determina il risultato mediante la funzione
    print(f"esito: {risultato}")  # stampa il risultato della mano
    if risultato == "pareggio":  # se il risultato è un pareggio
        punteggioPareggio["X"] = punteggioPareggio["X"] + punteggio_mano(carta_giocatore1, carta_giocatore2)
        # assegna alla chiave "X" nel dizionario il valore del punteggio delle carte
    if risultato == "vince giocatore 1":  # se il giocatore 1 vince la mano
        if punteggioPareggio[
            "X"] == 0:  # controlla che non ci siano punteggi nel dizionario dei pareggi da sommare (=0)
            punteggioG1 += punteggio_mano(carta_giocatore1, carta_giocatore2)  # quindi somma il punteggio delle carte
        elif punteggioPareggio["X"] != 0:  # se invece alla chiave "X" era stato assegnato un valore != 0
            punteggioG1 += punteggio_mano(carta_giocatore1, carta_giocatore2) + int(punteggioPareggio["X"])
            # somma il punteggio delle carte a quello assegnato alla chiave "X"
            # punteggioG1 += int(punteggioPareggio["X"])
            punteggioPareggio["X"] = 0  # avendo assegnato il valore, può tornare a 0
    # stesso lavoro per il giocatore 2
    elif risultato == "vince giocatore 2":
        if punteggioPareggio["X"] == 0:
            punteggioG2 += punteggio_mano(carta_giocatore2, carta_giocatore1)
        elif punteggioPareggio["X"] != 0:
            punteggioG2 += punteggio_mano(carta_giocatore2, carta_giocatore1) + int(punteggioPareggio["X"])
            # punteggioG2 += int(punteggioPareggio["X"])
            punteggioPareggio["X"] = 0
    print(f"punteggio G1: {punteggioG1}")  # stampa i punteggi alla fine di ogni mano
    print(f"punteggio G2: {punteggioG2}")
    n += 1  # incrementa l'indice
    inizio_mano = input("premere INVIO")
print(punteggioPareggio)  # stampa il dizionario dei pareggi, expected: {"X": 0}
# controllo punteggio finale
if punteggioG1 > punteggioG2:
    print("vince il giocatore 1")
elif punteggioG1 == punteggioG2:
    print("termina con un pareggio")
else:
    print("vince il giocatore 2")
