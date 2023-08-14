
document.body.innerHTML = "<h2>hola</h2>"
console.log('continuemos')
console.log('por favor')

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

areaTriangulo()
perimetroTriangulo()