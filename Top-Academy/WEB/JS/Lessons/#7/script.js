"use strict";

// function test(a, b, c){
//     return(b - a + c);
// }

// let x1 = 1, x2 = 2, x3 = 3;

// let res = test(x1, x2, x3);
// alert(res)



// function test2(n, m){
//     if(n / m == 0){
//         return "На ноль делить нельзя";
//     }
//     return n / m
// }

// let a1 = test2(10, 2);
// alert(a);
// let a2 = test2(10, 0);
// alert(a2)


// let a = +prompt("Введите 1-ое число");
// let b = +prompt("Введите 2-ое число")

// function pr(x, y){
//     if (x > y){
//         return x - y;
//     }
//     else{
//         return x + y;
//     }
// }

// console.log(pr(a, b))



// function sum(array){
//     let res = 0;
//     for(let index = 0; index < array.length; index++){
//         res += array[index];
//     }
//     return res
// }

// let array = [3, 7, 5, 0, 1, 8, 2, 4]
// console.log(sum(array))



// function max(array){
//     let max = array[0]; // 3
//     for (let index = 1; index < array.length; index++){
//         if (max < array[index]){
//             max = array[index];
//         }
//     } 
//     return max;
// }

// let array = [3, 7, 5, 0, 1, 8, 2, 4];
// console.log(max(array));


// let sum = function(a, b){
//     return a + b;
// }
// console.log(sum(1, 2))


// console.log(sum2(3, 4));
// function sum2(a, b){
//     return a + b
// }


// let a = (function(n){
//     console.log(n);
// })
// a(4)



// function func(a, b, c){
//     let res = (a * b / c);
//     return res;
// }
// console.log(func(5, 10, 6))


// let arrowfunc = (a, b, c) => (a * b / c);
// console.log(arrowfunc(5, 10, 6))


// let adaptive = (a, b, c) => {
//     let res = (a%2 + b**5 * c**2)
//     return res
// }
// console.log(adaptive(10, 5, 4))


// let hello = name => console.log(name);
// hello(12)



// (function(min, max){
//     console.log(Math.floor(Math.random() * (max - min) + min));
// })(2, 9);


// console.log(Math.floor(Math.random() * 9 + 7))



// let randWord = function(words){
//     return words[Math.floor(Math.random() * words.length)]
// }

// let array = ["Цикл", "Массив", "Условие", "Функция", "Класс"]
// console.log(randWord(array))



// let a = 5;

// if(a > 0){
//     let b = a + 6; 
//     console.log(b);
// }

// console.log(b)

// let j = 2

// function func(){
//     j = 3   
// }

// func()
// console.log(j)



document.write("<div id='block'></div>");
let id = document.getElementById("block");

id.style.width = id.style.height = "100px";

let createColor = () => {
    let r = Math.random() * 256;
    let g = Math.random() * 256;
    let b = Math.random() * 256;
    id.style.background = `rgb(${r}, ${g}, ${b})`;
}

createColor();