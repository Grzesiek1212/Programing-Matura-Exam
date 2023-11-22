with open('dane_geny.txt') as file:
    content = file.readlines()

for i in range(len(content)):
    content[i] = content[i].rstrip()

# 11111
print('1)')
counter = [0]*501
for genotyp in content:
    counter[len(genotyp)] += 1
c = 0
for number in counter:
    if number > 0:
        c += 1
print('gatunki:', c, 'najwiecej osobników:', max(counter))

# 22222


def ekstakcja_genow(gntp):
    geny = []
    while 'AA' in gntp and 'BB' in gntp and 'BB' in gntp[gntp.index('AA'):]:
        gntp = gntp[gntp.index('AA'):]
        geny.append(gntp[gntp.index('AA'):gntp.index('BB') + 2])
        gntp = gntp.replace(geny[-1], '')
    return geny


print('2)')
op = 0
for genotyp in content:
    for gen in ekstakcja_genow(genotyp):
        if 'BCDDC' in gen:
            op += 1
            break
print(op)

# 33333
print('3)')
op = 0
lon = 0
for genotyp in content:
    op = max(op, len(ekstakcja_genow(genotyp)))
    for gen in ekstakcja_genow(genotyp):
        lon = max(lon, len(gen))
print('najwiecej genów:', op, 'najdłuższy gen:', lon)

# 44444
print('4)')


def is_pal(text):
    return text == text[::-1]


def jaki_gnt(gggnt):
    if is_pal(gggnt):
        return 'S'
    if ekstakcja_genow(gggnt) == ekstakcja_genow(gggnt[::-1]):
        return 'O'
    else:
        return 'L'


Os = 0
Ss = 0
for genotyp in content:
    if jaki_gnt(genotyp) == 'S':
        Ss += 1
    bb1 = ''.join(ekstakcja_genow(genotyp))
    bb2 = ''.join(ekstakcja_genow(genotyp[::-1]))
    if bb1 == bb2:
        Os += 1
print('Silnie odporne:', Ss, 'Odporne:', Os)