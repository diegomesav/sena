function opcion (){
    return parseInt(prompt(`Seleccione el numero de la figura que desea consultar:
    1. Triangulo
    2. Rectangulo
    3. cuadrado
    4. Circulo`))
}

function areaPerimetro () {
    return prompt('por favor presiona "a" si deseas saber el area o "p" si deseas el perimetro:  ')
}
    

function areaTriangulo(){
    let base = parseFloat(prompt('Ingrese la base:  '))
    let altura =parseFloat(prompt('Ingrese la altura:  '))
    //document.body.innerHTML = "<h1>Time right now is:  " + d.getHours() + ":" + d.getMinutes() + ":" + d.getSeconds() + "</h1>"
    alert(`El area de ese triangulo es: ${(base*altura)}`)
}

function perimetroTriangulo(){
    let lado1 = parseFloat(prompt('Ingrese el lado 1:  '))
    let lado2 = parseFloat(prompt('Ingrese el lado 2: '))
    let lado3 = parseFloat(prompt('Ingrese el lado 3:  '))
    alert(`El perimetro de ese triangulo es: ${lado1 + lado2 + lado3}`)
}

function areaRectangulo(){
    let base = parseFloat(prompt('Ingrese la base:  '))
    let altura =parseFloat(prompt('Ingrese la altura:  '))
    alert(`El area de ese rectangulo es:${Math.round(base*altura)}`)
}

function perimetroRectangulo(){
    let base = parseFloat(prompt('Ingrese la base:  '))
    let altura =parseFloat(prompt('Ingrese la altura:  '))
    alert(`El perimetro de ese rectangulo es: ${Math.round(2*(base + altura))}`)
}

function areaCuadrado(){
    let lado = parseFloat(prompt('Ingrese la medida de un lado:  '))
    alert(Math.pow(lado,2))
}

function perimetroCuadrado(){
    let lado = parseFloat(prompt('Ingrese la medida de un lado:  '))
    alert(lado * 4)
}

function areaCirculo(){
    let radio = parseFloat(prompt('Ingrese la medida del radio:  '))
    alert(`El area de ese circulo es:  ${Math.round(Math.PI * (Math.pow(radio,2)))}`)
}


function perimetroCirculo(){
    let radio = parseFloat(prompt('Ingrese la medida del radio:  '))
    alert(`El perimetro de ese circulo es:  ${Math.round((Math.PI * radio * 2)) }`)
}

opcion = opcion()

if (areaPerimetro() == 'a'){
    switch(opcion){
        case 1:
            areaTriangulo()
            break
        case 2:
            areaRectangulo()
            break
        case 3:
            areaCuadrado()
            break
        case 4:
            areaCirculo()
            break 
    }
}
else{
    switch(opcion){
        case 1:
            perimetroTriangulo()
            break
        case 2:
            perimetroRectangulo()
            break
        case 3:
            perimetroCuadrado()
            break
        case 4:
            perimetroCirculo()
            break 
    }
}