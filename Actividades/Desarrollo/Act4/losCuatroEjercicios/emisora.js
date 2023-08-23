let oyentes = []
for(let i = 0; i < 6; i++){

    let oyente = {}
    oyente['nombre'] = prompt('Ingresa tu nombre:  ')
    oyente['cedula'] = prompt('Ingresa tu cedula:  ')
    oyente['fechaN'] = prompt('Ingresa tu fecha de nacimiento:  ')
    oyente['correo'] = prompt('Ingresa tu correo:  ')
    oyente['ciudadOr'] = prompt('Ingresa tu ciudad nde origen:  ')
    oyente['ciudadRes'] = prompt('Ingresa tu ciudada de residencia:  ')
    oyente['artistaFav'] = prompt('Ingresa tu artista favorito:  ')
    let canciones = {}
    alert('ingresa tus 3 canciones favoritas.')
    canciones['uno'] = prompt('1:  ')
    canciones['dos'] = prompt('2:  ')
    canciones['tres'] = prompt('3:  ')
    oyente['cancionesFav'] = canciones
    
    oyentes.push(oyente)
}
let og = 1-(parseInt(prompt("di un numero del 1 al 6 para elegir el oyente ganador:  ")))//og: oyente ganador

alert(`El ganador fue:
nombre:                ${oyentes[og].nombre}
cedula:                ${oyentes[og].cedula}
fecha de nacimiento:   ${oyentes[og].fechaN}
tu correo:             ${oyentes[og].correo}
ciudad de origen:      ${oyentes[og].ciudadOr}
ciudada de residencia: ${oyentes[og].ciudadRes}
artista favorito:      ${oyentes[og].artistaFav}
sus 3 canciones favoritas son:
${oyentes[og].cancionesFav.uno}
${oyentes[og].cancionesFav.dos}
${oyentes[og].cancionesFav.tres}`)