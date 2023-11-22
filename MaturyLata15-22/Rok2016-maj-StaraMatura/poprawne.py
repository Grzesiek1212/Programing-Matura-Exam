VERSE = 12
COLUMNS = 20

def importFile():
    file = open("gra.txt")
    lines = file.read().splitlines()
    file.close()

    twoDimensionalList = [[0]*COLUMNS for i in range(VERSE)]

    for i in range(VERSE):
        for j in range(COLUMNS):
            twoDimensionalList[i][j] = lines[i][j]

    return twoDimensionalList

def displayingList(gameOfLifeList):
    for i in range(VERSE):
        for j in range(COLUMNS):
            print(gameOfLifeList[i][j], end="")
        print()

def duplicateList(gameOfLifeList):
    superList = [[0]*COLUMNS*3 for i in range(VERSE*3)]
    for i in range(VERSE*3):
        for j in range(COLUMNS*3):
            superList[i][j] = gameOfLifeList[i%VERSE][j%COLUMNS]
    return superList

displayingList(duplicateList(importFile()))

def gameOfLife(gameOfLifeList, age):
    superList = duplicateList(gameOfLifeList)
    displayingList(gameOfLifeList)
    print()
    for whichAge in range(age-1):
        for i in range(VERSE,VERSE*2):
            for j in range(COLUMNS,COLUMNS*2):
                howManyAlives = 0
                #Tak nie robimy!!!
                # if superList[i-1][j-1] == "X":
                #     howManyAlives+=1
                # if superList[i-1][j] == "X":
                #     howManyAlives+=1
                # if superList[i-1][j+1] == "X":
                #     howManyAlives+=1
                # if superList[i][j-1] == "X":
                #     howManyAlives+=1
                # if superList[i][j+1] == "X":
                #     howManyAlives+=1
                # if superList[i+1][j-1] == "X":
                #     howManyAlives+=1
                # if superList[i+1][j] == "X":
                #     howManyAlives+=1
                # if superList[i+1][j+1] == "X":
                #     howManyAlives+=1

                for vx in range(-1,2):
                    for vy in range(-1,2):
                        if not (vx == 0 and vy == 0):
                            if superList[i+vx][j+vy] == "X":
                                howManyAlives +=1

                if superList[i][j] == '.' and howManyAlives==3:
                    gameOfLifeList[i - VERSE][j - COLUMNS] = 'X'
                elif superList[i][j] == 'X' and howManyAlives in [2,3]:
                    gameOfLifeList[i - VERSE][j - COLUMNS] = 'X'
                else:
                    gameOfLifeList[i - VERSE][j - COLUMNS] = '.'
        displayingList(gameOfLifeList)
        print()
        superList = duplicateList(gameOfLifeList)

def podA():
    gameOfLife(importFile(),37)

def podB():
    gameOfLife(importFile(), 2)

def podC():
    gameOfLife(importFile(), 100)

gameOfLife(importFile(),37)