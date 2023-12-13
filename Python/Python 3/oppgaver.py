# Oppgave 3.1
def helloWorld():
    print("Hello World!")

helloWorld()

# Oppgave 3.2
# Deklarere en funksjon er å lage en funksjon.
# Funksjonskall er å utføre en funksjon.
# Parametere er variabler du lager når du deklarerer en funksjon.
# Argumenter er verdier du gir parameterene til en funksjon når du kaller på den.
# Returverdi er det funksjonen sender tilbake når den er ferdig med oppgaven sin.
# Gloable variabler er variabler som blir deklarert utenfor en funksjon og kan brukes overalt i et program.
# Lokale variabler er variabler som blir deklarert i en funksjon og kan kun brukes i funksjonen de ble laget i.

# Oppgave 3.3
globalVar = "Dette er en global variabel"

def variabler():
    global globalVar

    localVar = "Dette er en lokal variabel."
    globalVar += " :)"

    return localVar

variabler()

print(globalVar)
print(variabler())

# Oppgave 3.4
def printTekst(x):

    for i in range(x):
        print("Hello World!")

printTekst(5)

# Oppgave 3.5
def bruttoLonn(timelonn, antallTimer):
    lonn = timelonn * antallTimer

    print(f'Med en timelønn på {timelonn} og {antallTimer} antall timer jobbet er bruttolønnen din {lonn}')

bruttoLonn(200, 37.5)

# Oppgave 3.6
def avgAge(num) -> float:
    total = 0

    for i in range(num):
        total += float(input("Skriv inn alder: "))
    
    average = total/num
    print(f'Gjennomsnittsalderen til de du har skrevet inn er {average}')

#avgAge(1)

# Oppgave 3.7
def checkText(string) -> str:
    string = string.lower()
    if "æ" in string or "ø" in string or "å" in string:
        print("JA")
    else:
        print("NEI")

#checkText("MÅNEN")

# Oppgave 3.8
def findChar(string,index) -> str:
    try:
        char = string[index]
        print(f'Karakteren på plass {index} er {char}')
    except IndexError:
        print(f'Plassen du har valgt er utenfor lengden til stringen.')

findChar("Hi thEre,hope you Like the Pool",20)

# Oppgave 3.9
def navn() -> str:
    fornavn = input("Skriv inn fornavnet og eventuelt mellomnavnet ditt: ")
    etternavn = input("Skriv inn etternavnet ditt: ")

    navn = fornavn + " " + etternavn

    return navn

#heltNavn = navn()
#print(heltNavn)

# Oppgave 3.10
def giveMeYourInfo(name) -> tuple:
    age: float = float(input(f"Hei {name}! Hvor gammel er du: "))
    location = input("Hva er ditt bosted: ")

    return age, location

#currentAge, currentLocation = giveMeYourInfo("Preben")

#print(currentAge, currentLocation)

# Oppgave 3.11
def math(x: float, y: float, type: str) -> float:
    '''
    Tar inn 2 tall og operasjon og regner ut svaret. Returnerer resultatet.
    '''
    if type == "/":
        if y != 0:
            return x / y
        else:
            return "Kan ikke dele på null"
    elif type == "//":
        if y != 0:
            return x // y
        else:
            return "Kan ikke gjøre heltallsdivisjon med null"
    elif type == "*":
        return x * y
    elif type == "%":
        if y != 0:
            return x % y
        else:
            return "Kan ikke gjøre modulus med null"
    else:
        return "Ugyldig operasjon. ALternativene er /, //, * eller %"

def runMath() -> float:
    '''
    Ber om 2 tall og operasjon og sender det til math() og får tilbake svaret.
    '''
    try:
        x: float = float(input("Skriv inn et tall: "))
        y: float = float(input("Skriv inn et tall til: "))
        type: str = input("Velg mellom / (divisjon), // (heltallsdivisjon), * (multiplikasjon) eller % (Finne rest etter deling): ")

        result = math(x, y, type)
        print(f'{x} {type} {y} = {result}')
    except ValueError:
        print("Ugyldig input. Vennligst velg gyldig tall og operator!")
    
runMath()

# Oppgave 3.12
def findFirstVowel(string: str) -> str:
    '''
    Finner den første vokalen i en streng og returnerer resultatet.
    '''
    vowels = "aeiouyæøåAEIOUYÆØÅ"

    for letter in string:
        if letter in vowels:
            return letter
    return "Ingen vokal funnet i teksten."

def mainVowel() -> str:
    '''
    Tar inn en streng og kjører findFirstVowel(string) og printer ut resultatet.
    '''
    string: str = input("Skriv inn noe tekst: ")
    result: str = findFirstVowel(string)
    print(f'Den første vokalen i teksten er: {result}')

