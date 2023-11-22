F = open("tekst.txt").read().split()

########################################################
### 73.1
ilosc = 0

for i in range(len(F)):
 if len(F[i]) > 1:
  for j in range(len(F[i])-1):
   if F[i][j] == F[i][j+1]:
    ilosc += 1
    break


print(ilosc)
print("\n")
#####################################################
### 73.2

Alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import math
iloscliter = 0
for j in range(len(F)):
 for z in range(len(F[j])):
  iloscliter += 1




for i in range(len(Alfabet)):
 ilosc = 0
 for j in range(len(F)):
  for z in range(len(F[j])):
   if Alfabet[i] == F[j][z]:
    ilosc += 1
 print(f"{Alfabet[i]}: {ilosc} ({round((100*ilosc)/iloscliter, 2)}%) ")
 # problem z zaokrąglaniem
print("\n")
##########################################################
### 73.3.
Samogloski = ['A', 'E', 'I', 'O', 'Y']
maks = 0

for i in range(len(F)):
 iloscspolglosek = 0
 k = 0
 for j in range(len(F[i])):
   if F[i][j] in Samogloski:
     iloscspolglosek = k
     k = 0
     if iloscspolglosek > maks:
      maks = iloscspolglosek
        if maks == 7:
            print(F[i])
   else:
    k += 1

print(maks)
