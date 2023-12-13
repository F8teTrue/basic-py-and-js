// Oppgave 1
const frukt = ["eple", "pære", "banan"];
const bær = ["jordbær","bringebær","blåbær"];
const combinedList = [];

for (let i = 0; i < frukt.length; i++){
    console.log(frukt[i])
}

frukt.splice(0,1,"kiwi")

for (let i = 0; i < frukt.length || i < bær.length; i++) {
    if (i < frukt.length) {
        combinedList.push(frukt[i]);
    }
    if (i < bær.length) {
        combinedList.push(bær[i]);
    }
}
for (let i = 0; i < combinedList.length;i++){
    document.getElementById("combinedList").innerHTML += `<li>${combinedList[i]}</li>`
}

// Oppgave 2
function snuSlangen(slangen){
    if (slangen.length <= 1){
        return slangen
    }

    slangen = slangen.reverse()

    return slangen
}

const opprinneligSlange = [1,2,3,4,5];
console.log(snuSlangen(opprinneligSlange));

// Oppgave 3
function findSmallest(num){
    // Splitter opp elementene i lista til individuelle elementer 
    // Bruker Math.min() til å finne det minste tallet
    const index = num.indexOf(Math.min(...num));

    return [num[index], index]
}

const numList = [41,6,15,98,13,2,9];
console.log(findSmallest(numList))

// Oppgave 4
let elevListe = [];

function leggTilElev() {
    let elevNavn = document.getElementById("elevNavn").value;

    // Sjekker om navnet allerede eksisterer i listen
    if (elevListe.indexOf(elevNavn) === -1 && elevNavn !== "") {
        elevListe.push(elevNavn);

        oppdaterElevListe();
    } else {
        alert("Elevens navn eksisterer allerede eller feltet er tomt!");
    }

    document.getElementById("elevNavn").value = "";
}

function oppdaterElevListe() {
    let listeElement = document.getElementById("elevListe");
    // Tømmer listen så ikke det samme blir lagt til når du legger til et nytt navn
    listeElement.innerHTML = "";

    // Legger til navn i lista i HTML
    for (let i = 0; i < elevListe.length; i++) {
        let navn = elevListe[i];
        document.getElementById("elevListe").innerHTML += `<li>${navn}</li>`
    }
}

// Oppgave 5
const scores = [];

function addScore(){
    const name = document.getElementById("name").value;
    const score = parseInt(document.getElementById("score").value);

    // Hvis name og score eksisterer og score er et tall, vil de bli lagt til som et nytt objekt i lista
    if (name && !isNaN(score)){
        const newScore = {name, score};
        scores.push(newScore);

        // Sorterer listen utifra score
        scores.sort((a,b) => b.score - a.score);

        // Tømmer HTML listen for å legge til den nye sorterte listen
        const scoreList = document.getElementById("scoreList");
        scoreList.innerHTML = "";

        // Sender navn og score til HTML for hvert objekt i listen
        for (let i = 0; i < scores.length; i++) {
            let nameOutput = scores[i].name;
            let scoreOutput = scores[i].score;
            document.getElementById("scoreList").innerHTML += `<li>${nameOutput} : ${scoreOutput}</li>`;
        }

        // Tømmer inputfeltene
        document.getElementById("name").value = "";
        document.getElementById("score").value = "";
    } else {
        alert("Vennligst skriv inn et gyldig navn og gyldig score!");
    };
};

// Map oppgaver

// Oppgave 7 nivå 1
const numbers = [1,4,7,9,14,74]
const dubbledNumbers = numbers.map(dubbleNum)

function dubbleNum(num){
    return num * 2;
}

console.log(numbers, dubbledNumbers)

//Oppgave 7 nivå 2
const firstNames = ["Herjus","Elias","Lukas","Preben"]
const firstLetters = firstNames.map(firstLetter => {
    return firstLetter[0];
});

console.log(firstNames, firstLetters)

// Oppgave 8
const aksjer = [
    { navn: 'CryptoTech', prisPerAksje: 90, sektor: 'kryptovaluta', antallAksjerTilgjengelig: 2000 },
    { navn: 'BioHealth', prisPerAksje: 160, sektor: 'bioteknologi', antallAksjerTilgjengelig: 0  },
    { navn: 'SpaceX', prisPerAksje: 120, sektor: 'romfart', antallAksjerTilgjengelig: 2500 },
    { navn: 'GreenEnergy', prisPerAksje: 190, sektor: 'fornybar energi', antallAksjerTilgjengelig: 3500 },
    { navn: 'TravelWays', prisPerAksje: 90, sektor: 'reiseliv', antallAksjerTilgjengelig: 1500 },
    { navn: 'AutoTech', prisPerAksje: 110, sektor: 'bilindustri', antallAksjerTilgjengelig: 2500 },
    { navn: 'EnergySun', prisPerAksje: 180, sektor: 'energi', antallAksjerTilgjengelig: 4000 },
    { navn: 'AquaTech', prisPerAksje: 70, sektor: 'vannbehandling', antallAksjerTilgjengelig: 0 },
    { navn: 'RoboTech', prisPerAksje: 200, sektor: 'robotikk', antallAksjerTilgjengelig: 1000 }
  ];

// Finner de forskjellige sektorene i listen
const sektorer = aksjer.map(aksje => {
    return aksje.sektor;
});

// Finner aksjer som koster mindre enn 100 enheter per aksje
const billigAksjer = aksjer.map(aksje => {
    if (aksje.prisPerAksje < 100){
        return aksje.navn;
    }
    // Filter er for å fjerne de tomme linjene som printes i console
}).filter(aksje => aksje);

const liteTilgjengelig = aksjer.map(aksje => {
    if (aksje.antallAksjerTilgjengelig == 0){
        return aksje.navn;
    }
    // Samme som forrige filter
}).filter(aksje => aksje);

// Finner den totale markedsverdien for hver aksje
const markedsverdi = aksjer.map(aksje => {
    const verdi = aksje.prisPerAksje * aksje.antallAksjerTilgjengelig;
    return `${aksje.navn}: ${verdi}`;
    // Join er for at det skal se bedre ut i konsollen ved å lage en ny linje for hver aksje
}).join('\n');


console.log(`De forskjellige sektorene er: \n${sektorer.join('\n')}`);
console.log(`Aksjene som koster mindre enn 100 enheter er: \n${billigAksjer.join('\n')}`);
console.log(`Aksjene som har 0 tilgjengelighet er: \n${liteTilgjengelig.join('\n')}`);
console.log(`Aksjene og deres totale markedsverdi:\n${markedsverdi}`);