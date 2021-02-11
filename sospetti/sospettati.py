file_presenze = open('presenze.txt', 'r')
file_sospettati = open('sospetti.txt', 'r')

def compilaDizionari (file_presenze) :
    contenutoPresenze = file_presenze.readlines()
    telefoni = dict()
    giorni = dict()
    for i in range(len(contenutoPresenze)) :
        line = contenutoPresenze[i].strip()
        campi = line.split(',')
        nome = campi[0]
        telefono = campi[1]
        telefoni[nome] = telefono
        inizioPeriodo = int(campi[2])
        finePeriodo = int(campi[3])
        periodo = []
        for number in range(inizioPeriodo, finePeriodo+1 ) :
            periodo.append(number)
            giorni[nome] = periodo

    return (telefoni, giorni)

def sospettati(nomeFile) :
    sospetti = []
    contenutoSospettati = nomeFile.readlines()
    for c in range(len(contenutoSospettati)) :
        nome = contenutoSospettati[c].strip()
        sospetti.append(nome)
    print(sospetti)
    return sospetti

def confronto(nomeSospetto, nomeDizionario) :
    contatto = []
    if nomeSospetto in nomeDizionario.keys() :
        periodo = set(nomeDizionario[nomeSospetto])
        nomeDizionario.pop(nomeSospetto)
        for chiave in nomeDizionario :
            giorniConfronto = set(nomeDizionario[chiave])
            if periodo.intersection(giorniConfronto) :
                print(chiave)
                contatto.append(chiave)

    elif  nomeSospetto not in nomeDizionario.keys() :
        contatto = ['no archivio']
    print(contatto)
    return contatto

def main() :
    # inizialzzaione dei dizionari
    (telefoni, giorni) = compilaDizionari(file_presenze)

    sospetti = sospettati(file_sospettati)

    for sospetto in sospetti :
        print(f'Contatti del cliente {sospetto} :')
        contatti = confronto(sospetto, giorni)
        contatti.sort()
        print(contatti)
        for persona in contatti :
            if contatti != [] and 'no archivio' not in contatti :
                numero = telefoni[persona]
                print(f'Contatto con {persona}, telefono {numero}')
            elif contatti == [] :
                print(f'il cliente {sospetto} non ha avuto contatti')
            elif contatti == ['no arch']:
                print(f"il cliente {sospetto} non è presente nell'archivio")

        print()
        print()

main()
