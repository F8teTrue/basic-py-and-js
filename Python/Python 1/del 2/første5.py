from random import randint 

def tall():
   

    while True:
        try:
            
            tall1 = input('Skriv inn et tall: ')        
            tall2 = input('Skriv inn et tall til: ')

            tall1 = float(tall1)
            tall2 = float(tall2)
            
            storre = tall1 > tall2

            if storre:
                print(f'{tall1} er større')
            else:
                print(f'{tall2} er større')
            break
        except ValueError:
            print('Ugyldig input. Skriv kun tall.')    

tall()

a = 1
b = 14.74
c = 857
d = -1
e = -7.54
f = -90

list = [a,b,c,d,e,f]
max = max(list)
min = min(list)
abs = abs(c)
avrund = round(b)

print(f'\nI denne listen: {list}')
print(f'Er maksverdien: {max}')
print(f'Minimum verdien er: {min}')
print(f'Tallet {b} avrundet er: {avrund}')
print(f'Absoluttverdien til tallet {c} er: {abs}\n')

navn = input('Skriv inn navnet ditt: ')

navn = navn.replace(' ','')
lengde = len(navn)

print(f'Lengden til navnet ditt er: {lengde}\n')


var = 50/3 > 20

if var:
    print('50 delt på 3 er større enn 20')
else:
    print('50 delt på 3 er ikke større enn 20')


#Mudulo fungerer som vanlig deling, men resultatet er hva som er igjen i rest.
num1 = 10%3
num2 = 17%2
num3 = 17%3
num4 = 17%6

print(f'10 delt å 3 har {num1} i rest')
print(f'17 delt å 2 har {num2} i rest')
print(f'17 delt å 3 har {num3} i rest')
print(f'17 delt å 6 har {num4} i rest\n')


var1 = randint(0,100)
var2 = randint(0,100)

if var1 > var2:
    print(f'Det første tallet: {var1}, er større enn det andre tallet: {var2}')
else:
    print(f'Det andre tallet: {var2}, er større enn det første tallet: {var1}')