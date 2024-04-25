//Para mandar um Alerta
window.alert("Ola Mundo");

// Para Mandar pro HTML
document.getElementById("myH1").textContent = "Ola Mundo";

let HelloWorld = "Ola Mundo";

document.getElementById(`Meu Caro, ${HelloWorld}`); // Crase`` faz poder colocar variaveis com ${}

let matema = 60;

document.getElementById("math").textContent = `Você é nota ${matema}`;

let windowalert = window.prompt("Window Prompt");
console.log(windowalert);

let sayanithing;
document.getElementById("buttonany").onclick = function () {
  // .onclick faz com que quando for clicado, seja acionado uma ação
  // function faz com que varias coisas aconteçam com um "estopim"
  sayanithing = document.getElementById("sayany").value; // .value pega o valor de "sayany"
  document.getElementById("txtany").textContent = sayanithing;
};

document.getElementById("Circus").onclick = function () {
  const pi = 3.14;
  let radius = window.prompt("Digite um Raio");
  radius = Number(radius);
  let somacircun = 2 * pi * radius;
  let somaarea = pi * radius ** 2;
  document.getElementById("circuarea").textContent = `A area é ${somaarea}`;
  document.getElementById(
    "circun"
  ).textContent = `A Cricunferencia é ${somacircun}`;
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
  text1.textContent = JSON.stringify(pessoa.name);

  var text2 = document.getElementById("text2");
  text2.textContent = JSON.stringify(pessoa.age);

  var text3 = document.getElementById("text3");
  text3.textContent = JSON.stringify(`${pessoa.likes} e ${pessoa.dislikes}`)
});

let chest = [
  {
      "nome": "GTA",
      "autor": "Future",
      "feat": "Metro Boomin"
  },
  {
      "nome": "Seen it All",
      "autor": "Future",
      "feat": "Metro Boomin"
  }
];

let chestjson = JSON.parse(chest); // Parse the JSON string into a JavaScript object
let nomeOfSecondItem = chestjson[1].nome; // Access the 'nome' property of the second item

let chesttostring = document.getElementById("chest");
chesttostring.textContent = nomeOfSecondItem; // Set the text content of the element to the value of nomeOfSecondItem

// fetch("./chest.json")
//   .then((response) => response.json())
//   .then((json) => console.log(json));
