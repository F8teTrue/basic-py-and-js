#Liste for å lagre tallene valgt av brukeren
tallListe = []

def kalkulator():
    while True:
        try:
            #Ber brukeren om et tall eller q for å gå videre
            tallValg = input('Skriv inn et tall eller "q" for å gå videre: ')

            #Sjekker om brukeren vil gå videre
            if tallValg.lower() == 'q':
                break
            
            #Gjør inputet til et float tall
            tall =float(tallValg)

            #Legger til tallet i listen
            tallListe.append(tall)
        
        except ValueError:
            print('Ugyldig tall.')
    
    #Sjekker om det er noen tall i listen
    if len(tallListe) > 0:
        #Regner summen av alle tallene i listen
        totalSum = sum(tallListe)

        #Skriver ut resultatet
        print('Summen av tallene er: ', totalSum)
    else:
        print('Du skrev ingen tall.')

    #Spør om brukeren vil legge til flere tall
    flerTall = input('Vil du legge til flere tall? (ja/nei): ')

    if flerTall.lower() == 'ja':
        #Starter funksjonen på nytt
        kalkulator()

    else:
        print('Hade :)')

kalkulator()

 