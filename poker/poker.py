from operator import itemgetter
from random import shuffle, randint



def estraiCarte(mazzo): #funzione per estrarre 5 carte dal mazzo
    numeri = [] #lista indici vuota *
    carteServite = [] #lista carte da servire vuota **
    while len(numeri) < 5: #finchè non ho 5 elementi nella lista indici
        indice = randint(0, 31) #estrae un indice a caso tra 0 e 31
        if indice not in numeri: #se l'indice estratto non è nella lista
            numeri.append(indice) #lo inserisce *
    for i in numeri: #scorre gli indici che ha estratto
        carteServite.append(mazzo[i]["valore"] + mazzo[i]["seme"]) #va a pescare nel mazzo (lista di dizionari) il dizionario
                                                                   #in posizione i e unisce i valori asseganti alle due chiavi
                                                                   #per formare una stringa che rappresenti la carta e la
                                                                   #appende alla lista delle carte da servire **
    return carteServite #restituisce la lista delle carte da servire

def sepCarte(tavolo): #gli fornisco le carte che sono sul tavolo
    lista = [] #lista vuota *
    for carta in tavolo: #itera le carte
        if len(carta) == 2: #controlla la lunghezza della stringa
            c = {"seme": carta[1], "valore": carta[0]} #crea un dizionario con una chiave "seme" e valore la seconda lettera
                                                       #della carta, e una chiave "valore" con la prima lettera della carta
            lista.append(c) #aggiunge il dizionario alla lista vuota *
        else:
            c = {"seme": carta[2], "valore": carta[0:2]} #stesso procedimento, cambia solo la lunghezza della stringa
                                                         #in caso sia più lunga di 2 caratteri (ex. 10P/F/Q/C)
            lista.append(c)

    return lista #restituisce la lista di dizionari


def dizionarioCarte(divise):
    valori = [] #lista vuota dei valori delle carte
    semi = [] #lista vuota dei semi delle carte
    lista = [] #lista vuota ausiliaria
    dizionarioV = {} #dizionario in cui vado a memorizzare i valori delle carte
    dizionarioS = {} #dizionario in cui vado a memorizzare i semi delle carte
    for carta in divise: #scorre la lista di dizionari separati per valori e semi delle carte
        valori.append(carta["valore"]) #aggiungo alla lista valori i valori associati a ogni chiave
        semi.append(carta["seme"]) #stessa cosa per i semi
    for i in valori: #scorro i valori
        if i not in dizionarioV: #se non sono nella lista li aggiungo
            dizionarioV[i] = 1 #quindi associo alla chiave il valore 1
        else:
            dizionarioV[i] += 1 #altrimenti se la chiave è già presente incremento il valore di 1
    for i in semi: #stesso procedimento per i semi
        if i not in dizionarioS:
            dizionarioS[i] = 1
        else:
            dizionarioS[i] += 1
    lista.append(dizionarioV)
    lista.append(dizionarioS)
    return lista #mi serve per ottenere due dizionari in cui tengo traccia delle carte uscite in base al valore e al seme
                 #e associare a ogni carta la quantità di quella carta per poter analizzare in seguito le combinazioni


def valore(carta): #associazione dei valori delle carte per comodità successiva
    if carta == '7' or carta == '8' or carta == '9' or carta == '10':
        return carta
    elif carta == 'J':
        return 11
    elif carta == 'Q':
        return 12
    elif carta == 'K':
        return 13
    elif carta == 'A':
        return 14


def combinazioni(combo):
    colore = [0] #lista del colore inizializzata a 0
    chiavePoker = "" #stringa della chiave del poker vuota
    for chiave in combo[1]: #analizzo il secondo dizionario, contenente i semi delle carte
        if combo[1][chiave] == 5: #se il valore associato è uguale a 5
            chiavePoker += chiave #modifica la stringa della chiave del poker con il nome del seme uscito
            colore[0] = 1 #modifica il valore in posizione 0, cambiandolo in 1 se si verifica la condizione sopra
    coppie = [0] #inizializzo a 0 le tre liste per coppie tris e poker
    tris = [0]
    poker = [0]
    for chiave in combo[0]: #analizzo ora il dizionario ocntenente i valori delle carte
        if combo[0][chiave] == 2: #se trovo una carta con valore associato 2, significa che è una coppia
            coppie[0] += 1 #incremento quindi il valore in posizione 0 della lista coppie
            coppie.append(chiave) #aggiungo in posizione 1 della stessa lista il valore della carta che compone la coppia*
        elif combo[0][chiave] == 3: #se invece ho 3 carte dello stesso valore
            tris[0] += 1 #incremento la lista del tris
            tris.append(chiave) #e ci appendo il valore della carta che compone il tris
        elif combo[0][chiave] == 4: #se invece ho 4 carte uguali
            poker[0] += 1 #incremento la lista del poker
            poker.append(chiave) #aggiungo alla lista il valore della carta che compone il poker
    if poker[0] == 1: #se il valore del poker è 1
        return f"poker di {poker[1]}" #unica combinazione e la restituisco in output
    elif tris[0] == 1: #stessa cosa per il tris
        return f"tris di {tris[1]}"
    elif coppie[0] == 1 and tris[0] == 0 and poker[0] == 0: #se invece si è incrementato solo l'indice della lista della coppia
                                                            #ed è uguale a 1
        return f"coppia di {coppie[1]}" #restituisco la coppia e anche il valore che ho appeso prima *
    elif coppie[0] == 2:
        return f"doppia coppia di {coppie[1]} e {coppie[2]}" #se le coppie sono 2, procedimento analogo
    elif coppie[0] == 1 and tris[0] == 1: #se si è incrementato anche il tris oltre alla coppia
        return f"full di {coppie[1]} e {tris[1]}" #restituisco un full con i valori appesi nelle liste in posizione 1
    scala = '78910JQKA' #inizializzo una stringa con l'ordine crescente delle carte **
    lista = [] #lista vuota °
    for chiave in combo[0]: #itero il dizionario di valori
        carta = {"chiave": chiave, "valore": int(valore(chiave))} #creo un sottodizionario con chiave "chiave e valore il valore
                                                                  #simbolico della carta, e una chiave "valore" con valore il
                                                                  #valore numerico della carta, calcolato con la funzione
        lista.append(carta) #appendo i dizionari alla lista °
    lista.sort(key=itemgetter("valore")) #ordino la lista di dizionari secondo l'ordine dei valori numerici, così riordino
                                         #anche le chiavi in ordine crescente grazie al valore algebrico assegnato
    sequenza = "" #inizializzo una stringa vuota
    for card in lista: #scorre la lista ordinata
        sequenza += card["chiave"] #aggiunge alla sequenza la chiave, per formare un'unica stringa
                                   #creando così una stringa da poter confrontare con la stringa scala **
    if sequenza in scala and (combo[1][chiavePoker] == 5): #controllo se la sottostringa è contenuta nella stringa della scala
                                                           #e che i semi siano tutti uguali (chiavePoker == 5)
        return f"scala reale di {chiavePoker}" #nel caso è scala reale
    elif sequenza in scala and (combo[1][chiavePoker] != 5): #se si verifica la corrispondenza con la scala ma non ha tutti
                                                             #i semi uguali
        return "scala" #è scala normale
    elif sequenza not in scala and (colore[0] == 1): #se non si verifica la corrispondenza con la scala ma i semi sono uguali
        return f"colore di {chiavePoker}" #ottengo colore
    else:
        return "nessuna combinazione" #altrimenti non si verifica nessuna combinazione

file = open("mazzoPoker.txt", "r") #apro il file in modalità lettura
file2 = open("mazzo_poker.txt", "w") #apro il file2 in modalità scrittura
lista = [] #lista vuota
for line in file:
    lines = line.strip().split()
    carte = {"seme": lines[1], "valore": lines[0]} #lista di dizionari con tutte le carte
    lista.append(carte) #appendi le carte alla lista
shuffle(lista) #mischia il mazzo
for carte in lista:
    print(carte["valore"], carte["seme"], file=file2) #riscrivi l'altro file con le carte mischiate
file2.close()
file_mazzo = open("mazzo_poker.txt", "r") #riapri il file nuovo in modalità lettura
mazzo = [] #mazzo vuoto
for line in file_mazzo:
    lines = line.strip().split()
    cards = {"seme": lines[1], "valore": lines[0]} #dizionario di carte
    mazzo.append(cards) #appendilo alla lista mazzo

tavolo = estraiCarte(mazzo) #tavolo composto da 5 carte che estraggo a caso
print(f"carte sul tavolo: ")
for i in tavolo:
    print(i) #le stampa a video sul tavolo
divise = sepCarte(tavolo) #separa le carte inserendole in una lista di dizionari
combo = (dizionarioCarte(divise)) #crea una lista di 2 dizionari, il primo ha come chiavi i valori delle carte
                                  #e come valori la quantità di quella carta
                                  #il secondo ha come chiavi i semi delle carte e come valori la quantità
#print(combo)
print(combinazioni(combo)) #stampa a video la combinazione uscita
