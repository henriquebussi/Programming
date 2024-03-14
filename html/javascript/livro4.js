//Para mandar um Alerta
window.alert("Ola Mundo")

// Para Mandar pro HTML
document.getElementById("myH1").textContent ='Ola Mundo'


let HelloWorld = "Ola Mundo"


document.getElementById(`Meu Caro, ${HelloWorld}`); // Crase`` faz poder colocar variaveis com ${}

let matema = 60

document.getElementById("math").textContent = `Você é nota ${matema}`

let windowalert = window.prompt("Window Prompt")
console.log(windowalert);

let sayanithing
document.getElementById("buttonany").onclick = function(){
    // .onclick faz com que quando for clicado, seja acionado uma ação
    // function faz com que varias coisas aconteçam com um "estopim"
    sayanithing = document.getElementById("sayany").value // .value pega o valor de "sayany"
    document.getElementById("txtany").textContent = sayanithing
}