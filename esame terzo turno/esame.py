file = open("leggi_di_murphy.txt", "r", encoding='utf-8')
lista_massime = []
for line in file:
    line = line.strip()
    lista_massime.append(line)
print(lista_massime)

dict = {}

for i in range(0, len(lista_massime)-1):
    if lista_massime[i][0].isupper() and lista_massime[i+1][0].isupper():
        dict[lista_massime[i]] = lista_massime[i+1]
    else:
        dict[lista_massime[i-1]] += lista_massime[i+1]

print(dict)
