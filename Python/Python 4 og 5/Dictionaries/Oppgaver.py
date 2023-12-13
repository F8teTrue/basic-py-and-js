# Oppgave 5.1
myInfo = {
    "bosted": "Oslo",
    "alder":  17
}
print(myInfo)

myInfo["skole"] = "Elvebakken"
print(myInfo)

# Oppgave 5.2
temperaturer = {
    "oslo": 0,
    "trondheim": -3,
    "bergen": 1,
    "tromsø": -6
}

for key in temperaturer:
    print(f'{key}: {temperaturer[key]}°C')

nyBy = input("Vil du legge til en ny by? (ja/nei): ").lower()

if nyBy == "ja":
    by = input("Skriv inn navnet til byen: ")
    temp = int(input(f"Skriv inn temperaturen i {by}: "))
    temperaturer[by] = temp

    print("Ny liste over byer med temperaturer:")
    for key in temperaturer:
        print(f'{key}: {temperaturer[key]}°C')
else:
    print("Hade :)")

# Oppgave 5.4
person = {'name': 'Alex','age': 17, 'drivers license': False, 'height': 175, 'sex': 'non-binary'} 

print("Alder:", person['age'])
print("Høyde:", person['height'])

userInput = input("Hva ønsker du å vite? (name, age, drivers license, height, sex): ").lower()

if userInput in person:
    print(f"{userInput}: {person[userInput]}")
else:
    print("Ugyldig nøkkel. Prøv igjen med en gyldig nøkkel fra dictionaryen.")

# Oppgave 5.5
person.pop("sex")

if "height" in person:
    print("Nøkkelen 'Height' finnes i dictinaryen.")
else:
    print("Nøkkelen 'Height' finnes ikke i dictinaryen.")

print("Nøkler i dictionaryen:")
print(person.keys())

print("Verdier i dictionaryen:")
print(person.values())

# Oppgave 5.6
aksjekurs = {'EQNR': 233.90, 'DNB': 210.50, 'NHY': 71.04, 'PMG': 18.52} 

for ticker in aksjekurs.keys():
    print(ticker)