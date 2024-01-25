// Para iniciar um arquivo .js é nescessario o NodeJS Instalado

// Abra apenas a pasta "javascript" e use o terminal do powershell

// para iniciar esse arquivo, escreva no terminal "node codelibrary.js"

// ou vá em "run" e "start debugging" e Nodejs

console.log("Exemplo \n") // console.log()


// Tipos de Variaveis

// var

var henrique = 'henrique' //declara uma variavel
var bussi = 'bussi' 
var santos = 'dos santos'

const tupa = "Manzano"

if (5 == 5){
    // let
    let henrique = 'henry'; //declara uma variavel "local", mas limitada a seu "bloco"/"escopo"
    let bussi = 'juan'; 
    let santos = 'guilherme'

    console.log(henrique, bussi, santos) 
    // Não se pode se redeclarar o let no mesmo bloco/escopo
} //dica: é recomendavel que se use let em "for"

// Variáveis declaradas são criadas antes de qualquer código ser executado. As variáveis não declaradas não existem até quando o código atribuir um valor a ela.

console.log(henrique, bussi, santos);

var henrique = 'Rodolpho'
var bussi = 'Trevisan'
var santos = 'Deborleda'

// const tupa = 'savero' // Da Erro, pois o const não pode ser renomeado

console.log(henrique, bussi, santos);
console.log(tupa);



// Tipos de Data (Data Types) são os tipos de data que uma variavel

var machine = "head" // String
var anvaged = 12 // Number
var bringhorizon = true // Boolean
var acdeci = 6.6 // Number
var bonovi = undefined // Undefined
var buletvalen = null // Null
var slitnot = 9007199254740991n // Bigint
var rastein = Symbol("duhast"); // Symbol

console.log(typeof machine); // Quando tem Texto
console.log(typeof anvaged); // Quando tem Numero Inteiro
console.log(typeof bringhorizon); // Quando ou é Verdade ou é Falso
console.log(typeof acdeci); // Quando tem Numero Racional
console.log(typeof bonovi);  // Quando Literalmente tem Nada
console.log(typeof buletvalen); // Quando não tem nada
console.log(typeof slitnot); // Quando tem MUITO Numero
console.log(typeof rastein); // Quando... sla, parece função ou algo do tipo



// Operadores Matemáticos

console.log("Soma: ", 10 + 2); // Soma
console.log("Subtração", 10 - 2); // Subtração
console.log("multiplicação", 10 * 2); // Multiplicação
console.log("a divisão é: ", 10 / 2 ); // Divisão


//Template strings

var crase = "Cristiano Ronaldo"
console.log('Meu nome é',
crase);
console.log(`Meu nome é 
${crase}`) // Utilizando Crase, você pode alterar a formatação do texto, alem de que com ${}, consegue operar comandos de melhor forma



// Array / Listas

const japa  = ["feio", "chines", "Inteligente"] // Isso é uma Array / Lista

console.log(japa);
console.log(japa.length); // .length diz quantos itens tem na Array
console.log(japa[2]); // Colocando [] depois da Array, conseguimos ver um item epecifico na Array
console.log(japa.push("corno")) // .push coloca um item no final de uma lista
console.log(japa.pop); // .pop remove o ultimo item de uma array



// for
for (let i of japa){ // of
    console.log(i);
}