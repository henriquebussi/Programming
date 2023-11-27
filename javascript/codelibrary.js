// Para iniciar um arquivo .js é nescessario o NodeJS Instalado

// para iniciar esse arquivo, escreva no terminal "node codelibrary.js"

console.log("Exemplo \n") // console.log()

// Tipos de Variaveis

// var

var henrique = 'henrique' //declara uma variavel
var bussi = 'bussi' 
var santos = 'dos santos'

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