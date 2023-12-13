function printTekst(navn){
    console.log("Hei",navn);
}

printTekst("Henrik")

//Terningkast med valgt antall sider
function dice(){
    let x = document.getElementById("diceSides").value;
    num = Math.floor(Math.random() * x + 1)
    document.getElementById("diceResult").innerHTML = "Du kastet: " + num
}


//Temperatur kalkulator
function celsiusToFahrenheit(celsius) {
    return celsius * 1.8 + 32;
}

function fahrenheitToCelsius(fahrenheit) {
    return (fahrenheit - 32) / 1.8;
}

function tempConvert() {
    const conversionType = document.getElementById("conversionType").value;
    const temperatur = parseFloat(document.getElementById("temperatur").value);
    let result;

    switch (conversionType) {
        case "celsiusToFahrenheit":
            result = celsiusToFahrenheit(temperatur);
            break;
        case "fahrenheitToCelsius":
            result = fahrenheitToCelsius(temperatur);
            break;
    }

    document.getElementById("result").innerHTML = result;
}


function setToColor() {
    let r = parseInt(document.getElementById("r").value);
    let g = parseInt(document.getElementById("g").value);
    let b = parseInt(document.getElementById("b").value);

    document.body.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;

    if (r+g+b < 175) {
        document.body.style.color = "white";
    }else {
        document.body.style.color = "black";
    }

    document.getElementById("rValue").innerHTML = r;
    document.getElementById("gValue").innerHTML = g;
    document.getElementById("bValue").innerHTML = b;
}


