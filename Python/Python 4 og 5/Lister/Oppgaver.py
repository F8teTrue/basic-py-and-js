# Oppgave 4.1
minListe = [1,2,3,4,5]
print(minListe)

# Oppgave 4.3
print(minListe[0:5:2])

# Oppgave 4.4
liste = [1,2,3,4,5,6,7,8,9,10]
print(liste)
liste[4] = "Femte elementet" # Det femte elementet har index 4
print(liste)
liste.append("Slutten")
print(liste)
liste.insert(4,"indeks 4")
del liste[8]
liste.pop()
print(liste)

# Oppgave 4.5
var = ['Hei', 'på', 'deg', '!']
for element in var:
    print(element)

# Oppgave 4.6
var = ['Hei', 'på', 'deg', '!']
for i in range(4):
    print(var[i])

# Oppgave 4.7
numList = [4,6,12,99,2,107]
print(min(numList))
print(max(numList))

# Oppgave 4.8 og 4.9
myNumbers: list[int] = [4,6,12,99,2,107]

def findBiggestNum(numList: list[int]) -> int:
    '''
    Finner det største tallet i en liste.
    '''
    biggestNum: int = numList[0]
    for i in range(len(numList)):
        if numList[i] - biggestNum > 0:
            print(f'Tallene som sammenlignes er {numList[i]} og {biggestNum}')
            print(f'Tallet som lagres er {numList[i]}')
            biggestNum = numList[i]
        elif numList[i] - biggestNum < 0:
            print(f'Tallene som sammenlignes er {numList[i]} og {biggestNum}')
            print(f'Tallet som lagres er {biggestNum}')
            biggestNum = biggestNum
        else:
            print(f'Tallene som sammenlignes er {numList[i]} og {biggestNum} og de er like.')
            biggestNum = numList[i]
    return biggestNum

print(f'Det største tallet i listen er {findBiggestNum(myNumbers)}')

# Oppgave 4.10
emptyList: list = []

def addToListAndSum(userList: list) -> list[float]:
    '''
    Lar bruker legge til float tall i en liste. Returnerer summen av listen.
    '''
    while True:
        userInput = input("Skriv inn et tall eller q for quit: ")
        if userInput.lower() == "q":
            break
        try:
            num: float = float(userInput)
            userList.append(num)
        except ValueError:
            print(f'{userInput} er ikke et tall eller q. Vennligst skriv inn et gyldig input.')
    return sum(userList)
    

addToListAndSum(emptyList)
userList = emptyList
totalSum: float = addToListAndSum(emptyList)

print(f'Listen med tall: {userList}')
print(f'Summen av tallene i listen er: {totalSum}')

# Oppgave 4.11

dager = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lørdag', 'Søndag']
temperaturer = [15, 18, 20, 17, 22, 16, 19]
vindhastighet = [5, 7, 6, 8, 4, 9, 5]
nedbørsmengde = [0.2, 0.0, 0.5, 0.0, 0.1, 0.0, 0.3]

for i in range(len(dager)):
    print(f'{dager[i]}: Temperatur: {temperaturer[i]}°C, Vindhastighet: {vindhastighet[i]} m/s, Nedbørsmengde: {nedbørsmengde[i]} mm')
