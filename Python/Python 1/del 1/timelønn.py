#Henter inn timelønn og hvor mange timer brukeren har jobbet
timelønn, timerJobbet = float(input('Skriv inn din timelønn: ')), float(input('Skriv inn timer jobbet: '))

#Regner ut bruttolønnen
brutto = timelønn * timerJobbet

print('Bruttolønnen din er: \n',brutto)

#Henter inn hvor mye brukeren skatter i prosent
skattProsent = float(input('Hvor mye prosent skatter du: '))

#Regner ut hvor mye skatt brukeren har betalt og hva som blir nettolønnen
skattBetalt = (brutto/100)*skattProsent
netto = brutto-skattBetalt

print('Du har betalt', skattBetalt, 'kroner i skatt.\n')
print('Din nettolønn er:', netto)
