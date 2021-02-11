infile = open("morse.txt", "r", encoding="cp1252")
testo = open("testo.txt", "r", encoding="cp1252")
codifica = open("codifica.txt", "w", encoding="cp1252")
dizionario = {}

for line in infile:
    line = line.split()
    dizionario[line[0]] = line[1]
infile.close()
for line in testo:
    line = line.split()

    lista_cod = []
    for i in line:
        i = i.upper()
        new_word = ""
        for j in i:
            new_word += dizionario[j] + " "
        lista_cod.append(new_word)
    print(lista_cod)

    parola = ""
    for word in lista_cod:
        parola += word + " "
    print(parola, file=codifica)
    print(line)
testo.close()
codifica.close()
