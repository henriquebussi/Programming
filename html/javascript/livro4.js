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

// fetch("chest.json")
//   .then(response => response.json())
//   .then(value => console.log(value))  
//   .catch(error => console.error('Error fetching JSON:', error));


let RandomBtn = document.getElementById("RandomBtn")
let RandomNumber = document.getElementById("RandomNumber")
let min = 10
let max = 50

RandomBtn.onclick = function(){
  let randomnum = Math.floor(Math.random() * (max - min) + min)
  RandomNumber.textContent = randomnum
}

let manyears = document.getElementById("manyears")
let textyears = document.getElementById("textyears")
let yearsubmit = document.getElementById("yearsubmit")


yearsubmit.onclick = function(){
  let ano1 = Number(manyears.value)
  if (ano1 < 18){
    textyears.textContent = "Não Autorizado"
  } else if(ano1 > 60){
    textyears.textContent = "...Porque?"
  }
  else{
    textyears.textContent = "Autorizado"
  }
}


let homosexual = document.getElementById("Homosexual")
let gay = document.getElementById("gay")
let dar = document.getElementById("Dar")
let viado = document.getElementById("Viado")
let none = document.getElementById("none")
let who = document.getElementById("who")
let resultado = document.getElementById("resultado")
let ternary = document.getElementById("ternary")
let ternaryresult = document.getElementById("ternaryresult")
let TarnaryBtn = document.getElementById("TarnaryBtn")
let onetoten = document.getElementById("onetoten")
let onetotenresult = document.getElementById("onetotenresult")
let onetotenBtn = document.getElementById("onetotenBtn")

who.onclick = function(){
  if(homosexual.checked || gay.checked || dar.checked || viado.checked){
    resultado.textContent = "Voce gosta de Homens"
  } else if(none.checked){
    resultado.textContent = "Voce gosta de mulheres"
  }
  else{
    resultado.textContent = "invalido"
  }
}

let diferente = 13

// Escrita Ternary, basicamente um shortcut de um if e else

TarnaryBtn.onclick = function(){
  let tarnary = (ternary.checked) ? "tarnary" : "Tininidad"
  ternaryresult.textContent = tarnary
}

// Switch, uma alternativa para muitos if's


onetotenBtn.onclick = function(){
  switch (onetoten.value){
    case "1":
      onetotenresult.textContent = "um";
      break;
    case "2":
      onetotenresult.textContent = "dois";
      break;
    case "3":
      onetotenresult.textContent = "tres";
      break;
    case "4":
      onetotenresult.textContent = "quatro";
      break;
    case "5":
      onetotenresult.textContent = "cinco";
      break;
    case "6":
      onetotenresult.textContent = "seis";
      break;
    case "7":
      onetotenresult.textContent = "sete";
      break;
    case "8":
      onetotenresult.textContent = "oito";
      break;
    case "9":
      onetotenresult.textContent = "nove";
      break;
    case "10":
      onetotenresult.textContent = "dez";
      break;
    default:
      onetotenresult.textContent = "digite novamente";
  }
}
let typenumber = document.getElementById('typenumber')
let typenumberBtn = document.getElementById("typenumberBtn")


typenumberBtn.onclick = function(){
  let temp = 0
  let math = 1
  console.log("funciona");
  let Numberty = Number(typenumber.value)
  for (let i = 0; i<Numberty; i++){ // for - faz um loop com alguns parametros, declarar, até onde vai, e se vai crescer
    console.log("velhobroxa");
    temp = temp + 1
    math = math * temp
    console.log("velhobroxa N°", temp);
    console.log("voce é um merda", math, "x");
  }
}


let array = [1, 2, 4 , 5, "aq"]
let object = {"xadrez": 1, "checkers": 0, "forsale": 22, "deardiary": "hi"}


// for in - percorre items em um objeto
for (let i in array){
    console.log(array[i]); 
}
for (let i in object){
    console.log(i,":", object[i]);
}
console.log('let in');

// for of -  percorre os valores de uma lista
for (let i of array){ 
    console.log(i)
}

try{
for(let i of object){
        console.log(i)    
}}
catch{
    console.log("não foi possivel");
}


let yes = document.getElementById('gameyes');
let no = document.getElementById("gameno");
let response = document.getElementById("gameresponse");
let preresponse = document.getElementById("prenumberfill");
let tenBtn = document.getElementById("totenBtn");
let result = document.getElementById("result");
let fill = document.getElementById("numberfill");
let onoff = true;
let loopresult = 1;
let i = 0;

function resultonclick(random) {
    let checkCondition = function() {
        if (i < loopresult) {
            tenBtn.onclick = function() {
                let value = fill.value;
                if (random == value) {
                    result.textContent = "Parabéns, tu acertou";
                    i = 1; // Update the loop condition
                } else {
                    result.textContent = "Errou!";
                }
            };

            // Request the next animation frame to continue checking the condition
            requestAnimationFrame(checkCondition);
        }
    };

    // Start checking the condition
    checkCondition();
}

yes.onclick = function() {
    response.textContent = ':), Então vamos jogar, tente adivinhar um número que eu estou pensando';
    no.disabled = true;
    no.style.color = 'grey';
    onoff = true;
    let random = Math.floor(Math.random() * 10);
    resultonclick(random);
};

no.onclick = function() {
    response.textContent = 'vai toma no seu cu, vamo jogar sim, quer saber, vai ser ainda mais dificil que o normal';
    yes.disabled = true;
    yes.style.color = 'grey';
    preresponse.textContent = "Tente acertar um número de 1 a 100 então otário";
    onoff = false;
    let random = Math.floor(Math.random() * 100);
    resultonclick(random);
};
