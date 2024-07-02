let array = [1, 2, 4 , 5, "aq"]
let object = {"xadrez": 1, "checkers": 0}


// for in - percorre items em um objeto
for (let i in array){
    console.log(array[i]); 
}
for (let i in object){
    console.log(object[i]);
}

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
// for (let i = 0; i++; i < array.lenght){
//     console.log(array[i]);
// }

