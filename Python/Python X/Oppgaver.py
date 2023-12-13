from random import randint as rand

# Oppgave X.1

def lagRutenett(rader,kolonner) -> list[list[int]]:
    '''
    Lager et rutenett med x antall rader og kolonner valgt av brukeren.
    '''
    rutenett: list = []
    for i in range(rader):
        rad: list = []
        for j in range(kolonner):
            rad.append(rand(1,10))
        rutenett.append(rad)

    for rad in rutenett:
        print(rad)

    return rutenett


# Oppgave X.2
def grådigAlgoritme(rutenett, rader, kolonner) -> int:
    '''
    En grådig algoritme som går gjennom et rutenett. Kan kun gå høyre og nedover. Returnerer antall poeng.
    '''
    posisjon = (0,0)
    score = rutenett[0][0]
    trekk = 0

    while posisjon != (rader -1,kolonner -1):
        høyre = 0
        nedover = 0
        
        # Sjekker om man kan bevege seg til høyre
        if posisjon[1] < kolonner - 1:
            høyre = rutenett[posisjon[0]][posisjon[1] + 1]

        # Sjekker om man kan bevege seg nedover
        if posisjon[0] < rader - 1:
            nedover = rutenett[posisjon[0] + 1][posisjon[1]]

        
        # Velger retningen som har høyest tall
        if høyre > nedover:
            posisjon = (posisjon[0], posisjon[1] + 1)
        else:
            posisjon = (posisjon[0] + 1, posisjon[1])

        # Finner scoren for posisjonen og legger det til i total score
        scoreForPosisjon = rutenett[posisjon[0]][posisjon[1]]
        score += scoreForPosisjon
        trekk +=1

        print(f'Trekk: {trekk} \n Posisjon: {posisjon} \n Total score: {score} \n Score for denne posisjonen: {scoreForPosisjon}')

    return score


def hovedFunksjon():
    rader: int = int(input("Skriv inn hvor mange rader du vil ha i rutenettet: "))
    kolonner: int = int(input("Skriv inn hvor mange kolonner du vil ha i rutenettet: "))
    rutenett = lagRutenett(rader, kolonner)
    score: int = grådigAlgoritme(rutenett, rader, kolonner)

    print(f'Total score ved målposisjonen ({rader - 1},{kolonner - 1}): {score}')


hovedFunksjon()