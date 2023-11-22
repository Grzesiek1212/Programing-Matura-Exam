F = open("dane_6_1.txt")
Dane = []
klucz = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
for line in F:
    Dane.append(line.rstrip())

for slowo in Dane:
    noweslowo = ''
    for i in range(len(slowo)):
        noweslowo += klucz[ord(slowo[i]) + 107 - 65]

    print(noweslowo)


