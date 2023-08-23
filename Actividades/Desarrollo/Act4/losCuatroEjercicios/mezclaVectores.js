//arr1 = [1,3,5,8]
//arr2 = [2,4,6,8]
let arr1 = []
let arr2 = []
let arr3 = []

let num1 = parseInt(prompt('Ingresa un numero a la lista 1: '))
arr1.push(num1)
for(let i = 0; i < 4; i++){
    let num = parseInt(prompt('Ingresa otro numero pero debe ser mayor al anterior:  '))
    if (num <= arr1[i]){
        while (num <= arr1[i]){
            num = parseInt(prompt(`Recuerda que debe ser mayor que ${arr1[i]}:  `))
        }
    }
    arr1.push(num)
}

let num2 = parseInt(prompt('Ingresa un numero a la lista 2: '))
arr2.push(num2)
for(let i = 0; i < 4; i++){
    let num = parseInt(prompt('Ingresa otro numero pero debe ser mayor al anterior:  '))
    if (num <= arr2[i]){
        while (num <= arr2[i]){
            num = parseInt(prompt(`Recuerda que debe ser mayor que ${arr2[i]}:  `))
        }
    }
    arr2.push(num)
}

for(let i = 0; i < 5; i++){

    if (arr1[i] < arr2[i]){
        arr3.push(arr1[i])
        arr3.push(arr2[i])
    }
    else{
        arr3.push(arr2[i])
        arr3.push(arr1[i])
    }
}

alert(arr3)
console.log(arr3)

let ordenado = false;
while(!ordenado) {
  ordenado = true;
  for(let i=0; i < arr3.length; i++) {
    if(arr3[i] < arr3[i-1]) {
      let temp = arr3[i];
      arr3[i] = arr3[i-1];
      arr3[i-1] = temp;
      ordenado = false;
    }
  }
}
alert(arr3)
console.log(arr3)