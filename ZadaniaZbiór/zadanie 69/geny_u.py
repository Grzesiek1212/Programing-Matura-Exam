genotypy = open("dane_geny.txt").read().split()

######## 69 1
dlg = [] #tablica zawierająca dlugosci genotypow
for i in genotypy:
    dlg.append(len(i))
odp1 = [len(set(dlg))]
maxi = 0
for i in dlg:
    p1 = dlg.count(i)
    if p1>maxi:
        maxi = p1
odp1.append(maxi)
print(odp1)

######## 69 2
def mutacja (geni):
    if "BCDDC" in geni:
        return True
    return False
def gen_z_genotypu (tab):
    flag = False
    g = []
    gen = ""
    for j in range(len(tab) - 1):
        if tab[j:j + 2] == "AA" and not flag:
            flag = True
            gen = ""
        if flag:
            gen += (str(tab[j]))
        if tab[j:j + 2] == "BB" and flag:
            gen += "B"
            flag = False
            g.append(gen)
    return g
odp2 = 0
geny = []
for i in genotypy:
    geny.append(gen_z_genotypu(i))
for i in geny:
    for j in i:
        if mutacja(j):
            odp2+=1
            break
print(odp2)
######### 69 3
maxiilosc = 0
maxidlg = 0
for i in geny:
    if len(i)>maxiilosc:
        maxiilosc = len(i)
    for j in i:
        if len(j)>maxidlg:
            maxidlg = len(j)
print(maxiilosc, maxidlg)
########## 69 4
silnieodp = 0
odporne = 0
def czy_sil_odp (a):
    if a == a[::-1]:
        return True
    return False
def czy_odp (a):
    if gen_z_genotypu(a) == gen_z_genotypu(a[::-1]):
        return True
    return False
for i in genotypy:
    if czy_sil_odp(i):
        silnieodp+=1
    if czy_odp(i):
        odporne+=1

print(odporne, silnieodp)