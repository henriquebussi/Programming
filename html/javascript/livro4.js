window.alert("Ola Mundo");

document.getElementById("myH1").textContent = "Ola Mundo";

let HelloWorld = "Ola Mundo";

document.getElementById("math").textContent = `Você é nota ${60}`;

let windowalert = window.prompt("Window Prompt");
console.log(windowalert);

let sayanithing;
document.getElementById("buttonany").onclick = function () {
    sayanithing = document.getElementById("sayany").value;
    document.getElementById("txtany").textContent = sayanithing;
};

document.getElementById("Circus").onclick = function () {
    const pi = 3.14;
    let radius = window.prompt("Digite um Raio");
    radius = Number(radius);
    let somacircun = 2 * pi * radius;
    let somaarea = pi * radius ** 2;
    document.getElementById("circuarea").textContent = `A area é ${somaarea}`;
    document.getElementById("circun").textContent = `A Cricunferencia é ${somacircun}`;
};

let Propernumber = document.getElementById("propernum");
let VarNum = 0;
const Increase = document.getElementById("IncreaseBtn");
const Decrease = document.getElementById("DecreaseBtn");
const Reset = document.getElementById("ResetBtn");

Increase.onclick = function () {
    VarNum++;
    Propernumber.textContent = VarNum;
};

Decrease.onclick = function () {
    VarNum--;
    Propernumber.textContent = VarNum;
};

Reset.onclick = function () {
    VarNum = 0;
    Propernumber.textContent = VarNum;
};

document.addEventListener("DOMContentLoaded", function() {
    const pessoa = {
        name: "Jon Arryn",
        age: "54",
        likes: "Governar",
        dislikes: "Ser morto"
    };

    var text1 = document.getElementById("text1");
    text1.textContent = pessoa.name;

    var text2 = document.getElementById("text2");
    text2.textContent = pessoa.age;

    var text3 = document.getElementById("text3");
    text3.textContent = `${pessoa.likes} e ${pessoa.dislikes}`;
});

fetch("./chest.json")
    .then((response) => response.json())
    .then((json) => {
        const chestDiv = document.getElementById("chest");
        json.forEach((item) => {
            const itemDiv = document.createElement("div");
            itemDiv.textContent = `Nome: ${item.nome}, Autor: ${item.autor}, Feat: ${item.feat}`;
            chestDiv.appendChild(itemDiv);
        });
    })
    .catch((error) => console.error('Error fetching JSON:', error));
