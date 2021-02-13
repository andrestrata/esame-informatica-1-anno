file = open("mappa.txt", "r")
tab  = []
for line in file:
    lines = line.strip().split()
    tab.append(lines)
dict = {}
for i in range(0, len(tab)):
    if i == 0:
        if tab[i][0] > tab[i][1] and tab[i][0] > tab[i+1][0] and tab[i][0] > tab[i+1][1]:
            coordinate = str(i)+ ' ' + str(0)
            dict[coordinate] = tab[i][0]
        if tab[i][-1] > tab[i][-2] and tab[i][-1] > tab[i+1][-1] and tab[i][-1] > tab[i+1][-2]:
            coordinate = str(i)+ ' ' + str(-1)
            dict[coordinate] = tab[i][-1]

        for j in range(1, len(tab[i])-1):
            if tab[i][j]> tab[i][j+1] and tab[i][j] > tab[i][j-1] and tab[i][j] > tab[i+1][j] and tab[i+1][j-1] and tab[i][j] > tab[i+1][j+1]:
                coordinate = str(i)+ ' ' + str(j)
                dict[coordinate] = tab[i][j]
    elif i != 0 and i != len(tab)-1:
        for j in range(0, len(tab[i])-1):
            if tab[i][j]> tab[i][j+1] and tab[i][j] > tab[i][j-1] and tab[i][j] > tab[i-1][j] and tab[i][j] > tab[i-1][j-1] and tab[i][j] > tab[i-1][j+1] and tab[i][j] > tab[i+1][j] and tab[i+1][j-1] and tab[i][j] > tab[i+1][j+1]:
                coordinate = str(i)+ ' ' + str(j)
                dict[coordinate] = tab[i][j]

    elif i == len(tab)-1:
        if tab[i][0] > tab[i][1] and tab[i][0] > tab[i-1][0] and tab[i][0] > tab[i-1][1]:
            coordinate = str(i)+ ' ' + str(0)
            dict[coordinate] = tab[i][0]
        if tab[i][-1] > tab[i][-2] and tab[i][-1] > tab[i-1][-1] and tab[i][-1] > tab[i-1][-2]:
            coordinate = str(i)+ ' ' + str(-1)
            dict[coordinate] = tab[i][-1]
        for j in range(1, len(tab[i])-1):
            if tab[i][j]> tab[i][j+1] and tab[i][j] > tab[i][j-1] and tab[i][j] > tab[i-1][j] and tab[i][j] > tab[i-1][j-1] and tab[i][j] > tab[i-1][j+1]:
                coordinate = str(i)+ ' ' + str(j)
                dict[coordinate] = tab[i][j]
cime = []
for key in dict:
    print("{} {} {}".format(dict[key], key[0], key[-1]))
    cime.append(int(dict[key]))
somma = 0
for x in cime:
    somma += x
media = somma/len(cime)
print(f"Altezza media: {media}")

