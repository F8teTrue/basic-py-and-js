def konverterData():
    while True:
        #Ber brukeren skrive noe som skal konverteres til en annen datatype
        dataInput = input("Skriv inn noe du vil konvertere til en annen datatype: ")

        #Spør brukeren om ønsket datatype
        datatype = input("Hvilken datatype vil du konvertere til? (int, float, str, bool): ").lower()

        #Prøver å konvertere dataen til ønsket datatype
        try:
            if datatype == "int":
                konvertertInput = int(dataInput)
            elif datatype == "float":
                konvertertInput = float(dataInput)
            elif datatype == "str":
                konvertertInput = str(dataInput)
            elif datatype == "bool":
                konvertertInput = bool(dataInput)
            else:
                print("Ugyldig datatypevalg. Kunne ikke konvertere.")
                continue

            # Skriv ut det brukeren skrev og den konverterte verdien
            print("Du skrev:",dataInput)
            print("Konvertert til",datatype,":",konvertertInput)
            print(type(konvertertInput))

            break 
        except ValueError:
            print("Kunne ikke konvertere til ønsket datatype. Prøv igjen.")

konverterData()

