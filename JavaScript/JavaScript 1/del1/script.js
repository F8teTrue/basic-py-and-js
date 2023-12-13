const hello = "Hello World!"

console.log(hello)

const navn = "Preben"

console.log("Hello", navn)

const pi = 3.14
const radius = 4

let omkrets;
omkrets = 2 * radius * pi

console.log(`For radius ${radius} er omkretsen ${omkrets}`)

const person = {
    navn: "Preben Egholm Dahl",
    alder: 17,
    bursdag: "30.07.06",
    voksen: undefined
}
if (person.alder >= 18) {
    person.voksen = true
} else {
    person.voksen = false
}

console.log(`Hello ${person.navn} du er ${person.alder} år gammel og er født ${person.bursdag}. Påstanden du er 18 år eller eldre er ${person.voksen}`)

let navnLengde

navnLengde = navn.length;
console.log(`Hello ${navn}. Ditt navn har ${navnLengde} bokstaver.`)

let fullNavnLengde

fullNavnLengde = person.navn.replace(/\s/g, "").length;
console.log(`Hello ${person.navn}. Ditt fulle navn har ${fullNavnLengde} bokstaver.`)

let fornavn
let mellomnavn
let etternavn
let fulltNavn

fornavn = "Preben "
mellomnavn = "Egholm "
etternavn = "Dahl "
fulltNavn = fornavn + mellomnavn + etternavn

console.log(`Hello ${fulltNavn}.`)
