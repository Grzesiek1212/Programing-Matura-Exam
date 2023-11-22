dane_geny_txt = open("dane_geny.txt")
geny = dane_geny_txt.read().split()



def most_common(tabela):
    mostcommon = 0
    for i in range(500):
        if tabela.count(i) > mostcommon:
            mostcommon = tabela.count(i)
    return mostcommon


ileg = 0
genydl = []
for gen in geny:
    if genydl.count(len(gen)) == 0:
        genydl.append(len(gen))
        ileg += 1
print(ileg)
gmax = 0
gendlwszystkie = []
for gen1 in geny:
    gendlwszystkie.append(len(gen1))
print(most_common(gendlwszystkie))



#geny = ["AABBED", "AADEDA", "DDAB", "DAB", "A", "AABDBDBD", "A", "ASDF"]
#gen = "DEAAEBDCBBAABCDDCECAABBCCBBCCDDDAACDDDBBCD"
def genotypy(a, wyn):
    wynik = wyn
    aind = a.find("AA")
    bind = a.find("BB")
    if aind < 0 or bind < 0:
        return wyn
    if aind < bind:
        wynik.append(a[aind: bind + 2])
        return genotypy(a[bind + 2:], wynik)
#    print(aind, bind, len(a), a)
    if bind + 2 <= len(a):
        return genotypy(a[bind + 2:], wynik)

#print(genotypy(gen, []))

#print(gen.find("AA") ,gen.find("BCDDC"), gen.find("BB"))

mutacje = 0
for gen1 in geny:
    tablicagenu = genotypy(gen1, [])
    for gen2 in tablicagenu:
        if gen2.find("BCDDC") >= 0:
            mutacje += 1
#print(mutacje)



iloscgenumax = 0
for g1 in geny:
    tablicagenu1 = genotypy(g1, [])
    if len(tablicagenu1) > iloscgenumax:
        iloscgenumax = len(tablicagenu1)
#print(iloscgenumax)

dlmax = 0
for g2 in geny:
    tablicagenu2 = genotypy(g2, [])
    for g3 in tablicagenu2:
        if len(g3) > dlmax:
            dlmax = len(g3)
#print(dlmax)


silnieodporne = 0
for el in geny:
    if el == el[::-1]:
        silnieodporne += 1
print("liczb silnie odpornych: " + str(silnieodporne))


odporne = 0
for element in geny:
    tg = genotypy(element, [])
    tgod = genotypy(element[::-1], [])
    if tg == tgod:
        odporne += 1
print("liczb odpornych: " + str(odporne))