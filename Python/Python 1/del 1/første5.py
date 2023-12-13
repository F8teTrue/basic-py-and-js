var = "Hello World!"

print(var,'\n')

a = 3
b = 6
c = a + b

print('Summen av', a, '+', b, 'er', c,'\n')

#Valgte å bruke kunn 2 variabler 
#Gjør selve gangingen i printen fordi da slipper jeg å lage en ny variabel
print(a, 'ganget med', b, 'er lik', a*b,'\n')

string = str(input('Skriv noe: '))

print(string*3,'\n')

print('Skriv kun tall')
temp1 = int(input('Skriv inn en temperatur: '))
temp2 =int(input('Skriv inn en temperatur til: '))
temp3 = int(input('Skriv inn en temperatur siste gang: '))

tempAvg = int((temp1 + temp2 + temp3) /3)

print('\nGjennomsnittet av temperaturene er: ')
print(tempAvg,'\n')


