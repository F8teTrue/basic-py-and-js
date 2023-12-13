let inputTekst = ' '
document.getElementById('minInput').value = inputTekst;

function sendInn(){
    let x = document.getElementById('minInput').value;
    let g = document.getElementById("checkBox");
    if (x >= 16 && g.checked == true){
        alert("Du kan øvelseskjøre :)")
    }else if(x >= 25){
        alert("Du kan øvelseskjøre :)")
    }else if (x < 16 && g.checked == true){
        alert("Du er ikke gammel nok enda til å øvelseskjøre :(")
    }else if (x >= 16 && g.checked == false){
        alert("Du mangler grunnkurs for å kunne øvelseskjøre!")
    }else{
        alert("Du må være minst 16 år gammel og ha grunnkurs for å kunne øvelseskjøre!")
    }
    
    document.getElementById("minInput").value = "";
    g.checked = false;
}

let tall = 1
console.log("1-10 uten løkker:")
function printTall() {
    if (tall <=10){
        console.log(tall)
        printTall(tall++)
    }
}
printTall()

let tall2 = 1

console.log("1-10 med while-løkke:")
while (tall2 <=10){
    console.log(tall2);
    tall2++;
}

console.log("1-10 med for-løkke:")
for (let i = 1; i <=10; i++) {
    console.log(i);
}


function numPrint(){
    let userInput = document.getElementById("numInput").value;
    let numList = "";

    for (let i = 1; i <= userInput; i++){
        numList += i + " ";
    }

    document.getElementById("numList").innerHTML = "Tallene fra 1 til " + userInput + " er: " + numList;
}

const person = {
    navn: "Preben Egholm Dahl",
    alder: 17,
    bursdag: "30.07.06",
    voksen: undefined
}

const personInfoObject = document.getElementById("personInfo");

for (const key in person){
        personInfoObject.innerHTML += `<p>${key}: ${person[key]}</p>`;
}


function passordGen() {;
    let passord = document.getElementById("passord").value;
    
    for (let bokstav of passord) {;
        if (bokstav.toUpperCase() == "E") {;
            passord = passord.replace(bokstav, "3");
        };
        if (bokstav.toUpperCase() == "I") {;
            passord = passord.replace(bokstav, "1");
        };
        if (bokstav.toUpperCase() == "O") {;
            passord = passord.replace(bokstav, "0");
        };
    };
    
    for (let bokstav of passord){
        let random = Math.floor(Math.random() * 2);
        if (random === 0){;
            passord = passord.replace(bokstav, bokstav.toLowerCase());
        }else{
            passord = passord.replace(bokstav, bokstav.toUpperCase());
        };
    };
    const symboler = "!#$%&/()=?+€§|{}≈≠¿±[]";
    for (let x = 0; x < 3; x++) {;
        let randomSymbol = symboler[Math.floor(Math.random() * symboler.length)];
        passord += randomSymbol;
    }
    console.log(passord);
}



