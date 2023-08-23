let edades = []
let menores = 0
let adultos = 0
let adultosM = 0
let sumEdades = 0

for(let i = 0; i < 10; i++){

    let edad = 0
    while (edad < 1 || edad > 120){
        
        edad = parseInt(prompt("Ingrese su edad: (min 1, max 120):  "))
        if (edad < 1 || edad > 120){
            alert('Mmmmm no te creo, vuelve a ingresar')
        }
        else if (isNaN(edad)) {
            alert("Por favor ingrese un numero valido entre 1 y 120:  ")
            edad = 0
        }
    }
    edades.push(edad)
}

for (const i of edades){

    if (i < 18){menores += 1}
    else if (i >= 18 && i < 60){adultos += 1}
    else{adultosM += 1}
        
    sumEdades += i
}


alert(`Ingresaron ${menores} menores, ${adultos} adultos y ${adultosM} adultos mayores`)

alert(`la mayor edad ingesada fue ${Math.max(...edades)} años`)

alert(`la menor edad ingesada fue ${Math.min(...edades)} años`)

alert(`El promedio de edades fue ${sumEdades / (edades.length)} años`)