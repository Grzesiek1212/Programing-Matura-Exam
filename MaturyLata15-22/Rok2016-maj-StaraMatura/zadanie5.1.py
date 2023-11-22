F = open("gra.txt")
Pokolenie = F.read().split()
print(Pokolenie)
def Lewagora(i, j, Pokolenie1):
    if (i - 1) < 0:
        if j - 1 < 0:
            return Pokolenie1[11][19]
        else:
            return Pokolenie1[11][j-1]
    else:
        if j - 1 < 0:
            return Pokolenie1[i-1][19]

        else:
            return Pokolenie1[i-1][j-1]

def Gora(i, j, Pokolenie1):
    if (i - 1) < 0:
        return Pokolenie1[11][j]
    else:
        return Pokolenie1[i-1][j]

def Prawagora(i, j, Pokolenie1):
    if (i - 1) < 0:
        if j + 1 > 19:
            return Pokolenie1[11][0]
        else:
            return Pokolenie1[11][j+1]
    else:
        if j + 1 > 19:
            return Pokolenie1[i-1][0]

        else:
            return Pokolenie1[i-1][j+1]

def Lewy(i, j, Pokolenie1):
    if (j - 1) < 0:
        return Pokolenie1[i][19]

    else:
        return Pokolenie1[i][j-1]

def Prawy(i, j, Pokolenie1):
    if (j + 1) > 19:
        return Pokolenie1[i][0]

    else:
        return Pokolenie1[i][j + 1]

def Dol(i, j, Pokolenie1):
    if (i + 1) > 11:
        return Pokolenie1[0][j]
    else:
        return Pokolenie1[i+1][j]

def Lewadol(i, j, Pokolenie1):
    if (i + 1) > 11:
        if j - 1 < 0:
            return Pokolenie1[0][19]
        else:
            return Pokolenie1[0][j-1]
    else:
        if j - 1 < 0:
            return Pokolenie1[i+1][19]

        else:
            return Pokolenie1[i+1][j-1]

def Prawadol(i, j, Pokolenie1):
    if (i + 1) > 11:
        if j + 1 > 19:
            return Pokolenie1[0][0]
        else:
            return Pokolenie1[0][j+1]
    else:
        if j + 1 > 19:
            return Pokolenie1[i+1][0]

        else:
            return Pokolenie1[i+1][j+1]

def LiczenieSasiad(i,j,Pokolenie):
    licznik = 0
    if Lewagora(i,j,Pokolenie) == 'X':
        licznik += 1
    if Gora(i,j,Pokolenie) == 'X':
        licznik += 1
    if Prawagora(i,j,Pokolenie) == 'X':
        licznik += 1
    if Lewy(i,j,Pokolenie) == 'X':
        licznik += 1
    if Prawy(i,j,Pokolenie) == 'X':
        licznik += 1
    if Lewadol(i,j,Pokolenie) == 'X':
        licznik += 1
    if Prawadol(i,j,Pokolenie) == 'X':
        licznik += 1
    if Dol(i, j, Pokolenie) == 'X':
        licznik += 1

    return licznik

def Transformcja(Pokolenie):
    NowePokolenie = []
    for i in range(len(Pokolenie)):
        nowywiersz=''
        for j in range(len(Pokolenie[i])):
            Sasiady = LiczenieSasiad(i, j, Pokolenie)
            if Pokolenie[i][j] == '.':
                if Sasiady == 3:
                    nowywiersz += 'X'
                else:
                    nowywiersz += '.'

            if Pokolenie[i][j] == 'X':
                if Sasiady == 2 or Sasiady == 3:
                    nowywiersz += 'X'
                else:
                    nowywiersz += '.'

        NowePokolenie.append(nowywiersz)
    return NowePokolenie


for i in range(36):
    Pokolenie = Transformcja(Pokolenie)


print(LiczenieSasiad(1, 18, Pokolenie))