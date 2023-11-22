F = open('bledne.txt')

ciagi = []

for line in F:
    if len(line) > 4:
        ciagi.append(line.split())


#######################################################################
### 61.3

for i in range(len(ciagi)):
    delta0 = (int(ciagi[i][1]) - int(ciagi[i][0]))
    delta1 = (int(ciagi[i][2]) - int(ciagi[i][1]))
    delta2 = (int(ciagi[i][3]) - int(ciagi[i][2]))
    delta3 = (int(ciagi[i][4]) - int(ciagi[i][3]))

    if delta0 != delta1 and delta1 == delta2 == delta3:
        print(ciagi[i][0])

    if delta0 != delta1 and delta1 != delta2 and delta2 == delta3:
        print(ciagi[i][1])

    if delta0 != delta1 and delta1 != delta2 and delta2 != delta3 and delta3 == delta0:
        print(ciagi[i][2])

    if delta0 == delta1 == delta2:

        for j in range(1, len(ciagi[i])-1):
            if int(ciagi[i][j]) + delta0 != int(ciagi[i][j+1]):
                print(ciagi[i][j+1])
                break



