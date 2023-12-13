for i in range(5):
    print("Dette printes!")


# Oppgave 2.2
# En string brukes for å representere tekst og brukes hele tiden innenfor koding.
# En integer brukes for å representere hele tall og brukes også veldig mye i koding. F.eks. 'alder = 17'
# En float brukes for tall med desimaler som f.eks. priser, lengder og vekt.
# Boolean brukes for å representere to mulige tilstander, True eller False. F.eks. 'erVoksen = False'

num = 0

while num <= 7:
    print(num)
    num +=1

tall = 10
fortsett = True

while fortsett:
    print(tall)
    tall += 1

    if tall > 20:
        fortsett = False

print('')

list = []

while True:
    userInput = input('Skriv noe eller "Exit" for å avslutte: ')
    userInput = userInput.lower()

    if userInput == "exit":
        break
    else: 
        list.append(userInput)
        continue

print(f'Det du skrev er følgende: \n {list}')

num1 = 0

for i in range(5):
    print(f'{num1} * 1 = {num1}')
    num1 += 1 

print('')

for i in range(5,10):
    print(i)

print('')

for i in range(0,11,2):
    print(i)

print('')

for i in range(5,0,-1):
    print(i)

tekst = "Hello World!"

if "e" in tekst:
    print('Teksten inneholder bokstaven "e"')
else:
    print('Teksten inneholder ikke bokstaven "e"')

print('')

text = 'Uten mat og drikke, duger helten ikke'
vokaler = 'aeiouyæøå'

# Skriv ut alle vokaler i teksten
print("Vokaler i teksten:")
for bokstav in text:
    if bokstav.lower() in vokaler:
        print(bokstav, end=' ')

# Skriv ut alle konsonanter i teksten
print("\nKonsonanter i teksten:")
for bokstav in text:
    if bokstav.lower() not in vokaler:
        print(bokstav, end=' ')

print('\n')
for i in range(1, 10):
    print(i, end =" ")
    if i % 3 == 0:
        print('')


print('')
for i in range(1,11):
    if i == 6:
        print('Hopper over')
        continue
    else:
        print(i)

tall2 = 0
for i in range(10, 21):
    if tall2 > 50:
        print(f'Tallet {tall2} er større enn 50.')
        break
    else:
        print(f'{tall2} + {i} = {tall2 + i} ')
        tall2 += i