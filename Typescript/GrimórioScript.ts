import prompt from 'prompt-sync';
const input = prompt();
//não se esqueça de dar o NPM nas bibiliotecas

//boolean 
//number
//string
//null
//any

// var | let = variavel
var texto:string|number;
var espaco:string

texto = "text"
espaco = "\n /////////////////////////////////////////////////////////////// \n"
//console.log =  print
console.log(texto);
console.log(espaco);

//prompt = input (obs: precisa do require "prompt-sync")

// == igual
// === IGUAL | Considera o Tipo do Dado
// > Maior 
// < Menor
// >= Maior ou Igual
// <= Menor ou Igual
// != Diferente
// !== Diferente | Considera o Tipo de Dado


// console.log(10 === "10");
// console.log(10 == "10");
// console.log(10 != "10");
// console.log(10 !== "10");
// console.log("JOAO" !== "joao");
// console.log(50 > 20);

console.log(espaco);

// Operaradores Relacionais
//&& e
//|| ou
//! não
console.log("Operaradores Relacionais \n")
// console.log("joao" == "JOAO" && 20 > 10);
// console.log("joao" == "JOAO" || 20 > 10);
console.log(!(20 > 10));
console.log(20 > 10);
console.log(!(20 < 10));

console.log(espaco);

// if() {}
// else if() {}
// else {}

console.log("IF e ELSE \n");
var idade = Number(prompt("Digite sua idade: "));
if(idade < 18) {
  console.log("Proibido Entrada no Site")
} else {
  console.log("Bem vindo kkk")
}
console.log(espaco);

console.error("errei fui mlk")
// confirm - mensagem do window
// console.error - mensagem de erro
// window.prompt - Caixa de resposta no windows / prompt do window


// //If "On Line" / Uma Linha

const idadeonline = 20;
const idadeGrouponline = idade < 18 ? "Criança" : "Adulto";
console.log(idadeGrouponline);

//while

var contador = 0;

while (contador <= 20) {
  console.log(contador);
  contador += 1
}
// += 1 ou ++ = contador = contador + 1

// do{}...while - "faça enquanto o while estiver certo" / do THIS while 
// for - tipo o "for" do python, só que mais complicado e chato

console.log(espaco)

var listas = ["Joao", 23, true, ['1','2','3'], null];

console.log(listas[0])
console.log(listas[3])
console.log(listas[3][2])
console.log(listas[listas.length -1])

//listas[] - que nem no python
//.length - da para ver o ultimo


//for 3 parametord: (uma var; uma condição; instrução para todo loop)

console.log(espaco)

for (var contador = 0; contador < listas.length; contador++) {
  console.log(contador);
  console.log(listas[contador])
}

for(let i in listas) {
  console.log(i) // IN: i é o indice (0,1, ..)
}

for(let i of listas) {
  console.log(i) // OF: i é o item (a, b, ..)
} 
//push: tipo append do python, adiciona em lista



// Matriz "Coordenada" - Acontece em uma matriz 2xNumber(qualquer numero da certo), e é basicamente x e y; se utiliza dois for para cada(x, y), um dentro do outro [Suggestion: "LISTAexerciesScript" e "listav2Script"]

//obs, For dentro de For apenas quando tem duas dimensões
console.log(espaco)

const matrizA: number[][] = [
  [1, 2],
  [3, 4]
]
const matrizB: number[][] = [
  [5, 6],
  [7, 8]
]
const matrizTotal: number[][] = [
  [],
  []
]

for (var x in matrizA) {
  for (var y in matrizA) {
    matrizTotal[x][y] = matrizA[x][y] * matrizB[x][y];
  }
}
console.log(matrizTotal)

console.log(espaco)

//function - tipo o def do python [Suggestion: "functionScript"]

function verificarParOuImpar(num1:number):
  void{
    if (num1 % 2 == 0) {
      console.log(num1, 'é par')
    } else{
      console.log(num1, 'é impar')
    }
  }
verificarParOuImpar(8)

// const idade = console.log("23") está ERRADO, no TS, não se consegue guardar como variavel

//indexof


async function minhaFuncaoAssincrona(): Promise<string> {
  // Lógica assíncrona aqui
  // Pode ser uma chamada de API, acesso a banco de dados, etc.

  // Aguardar um tempo simulado usando a função setTimeout
  await new Promise(resolve => setTimeout(resolve, 2000));

  // Retornar um valor
  return "Resultado da função assíncrona";
}

minhaFuncaoAssincrona().then(resultado => {
  console.log(resultado); // "Resultado da função assíncrona"
}).catch(erro => {
  console.error(erro);
});
