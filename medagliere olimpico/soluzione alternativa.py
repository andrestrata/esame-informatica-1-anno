# NOTA: i file specificati nell'esercizio NON sono visibili direttamente,
# ma esistono e si possono aprire (i nomi sono quelli indicati nel testo)

"""
nazioni = {}

per ogni riga
    leggi nazione
    leggi e calcola medaglie realtive
    se nazione in nazioni
        aggiorna nazione
    altrimenti
        aggiungi nazione con medaglia relativa

stampa lista nazioni
ordina nazioni per medaglie
stampa le prime tre
"""

from operator import itemgetter


def medagliaRelativa(posizione):
    # 1 --> 1, 2 --> 0.1, 3--> 0.05, 4--> 0
    punti = [0, 1, 0.1, 0.05]

    if posizione > 3:
        posizione = 0

    return punti[posizione]


def main():
    # apertura file
    file = open("nazioni.txt", "r")

    # dichiarazione strutture dati
    nazioni = dict()

    for line in file:
        parts = line.strip().split()

        nazione = parts[2]
        punti = medagliaRelativa(int(parts[3]))

        if nazione in nazioni:
            nazioni[nazione] = nazioni[nazione] + punti
        else:
            nazioni[nazione] = punti

    file.close()
    # nazioni contiene tutte le informazioni, le stampo
    print("Medaglie d'oro equivalenti:")
    for nazione in nazioni:
        if nazioni[nazione] > 0:
            print(nazione, f"{nazioni[nazione]:.2f}")

    ordinate = sorted(nazioni.items(), key=itemgetter(1), reverse=True)

    print("Le prime tre nazioni del medagliere sono:")
    for i in range(3):
        (nazione, punti) = ordinate[i]
        print("\t", i + 1, ")", nazione)


main()
