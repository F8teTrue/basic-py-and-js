let num1
let num2

function tallPrompt() {
    num1 = parseInt(prompt("Skriv inn et tall: "))
    num2 = parseInt(prompt("Skriv inn et tall igjen: "))

    if (num1 > num2) {
        alert(`${num1} er større enn ${num2}`)
    } else if (num1 < num2){
        alert(`${num2} er større enn ${num1}`)
    } else {
        alert(`Tallene er like :)`)
    }
}

let alder

function alderSjekk() {
    alder = parseInt(prompt("Skriv inn alderen din: "))


    if (alder >= 18) {
        alert(`Du er gammel nok til å stemme :)`)
    } else {
        alert(`Du er ikke gammel nok til å stemme!!!`)
    }
}

let passord

function passordSjekk() {
    passord = prompt("Skriv inn passord: ")

    if (passord == "passord123") {
        alert("Tilgang innvilget :)")
    } else {
        alert("Tilgang nektet!")
    }
}

let lines
let randLineNum

async function getLine() {
    const util = require("util");
    const fs = require("fs");
    const readFile = util.promisify(fs.readFile);
    const fileContent = await readFile("./tekstFiler/jokes.txt", "utf-8");
    lines = fileContent.split("\n")
    console.log(fileContent)
    randLineNum = Math.floor(Math.random() * lines.length);
    return(lines[randLineNum]);
}
module.exports = getLine();
