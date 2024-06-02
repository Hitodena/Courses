"use strict";
// let i = 1
// do {
//     document.write("Квадрат " + i + " равен " + i**2 + "<br>")
//     i = i + 1
// } while (i < 8);



// let i = 0
// while (i < 8) {
//     document.write("Квадрат " + ++i + " равен " + i**2 + "<br>")
// }



// let sum = 0
// let i = 0
// do {
//     sum += parseInt(prompt(`Введите ${++i} число: `))
// } while (i <= 2);
// document.write(`Сумма: ${sum}`)



// let ch = 0
// do{
//     ch += +(prompt("Введите число: "))
// } while (ch > 0);
// alert("Сумма: " + ch)

// let ch = 0;
// ch = +prompt("Введите число: ");
// while(ch > 0){
//     ch = +prompt("Введите число: ");
// }
// alert("Сумма: " + ch)



// let n = 1
// while(n <= 20){
//     n++
//     if(n % 2 == 0){
//         document.write(n + "<br>")
//     }
// }



// let start = 5;
// let end = 10;
// let sum = 0;
// while(start <= end){
//     sum += start;
//     start++;
// }
// document.write(sum);




// let i = 3;
// while(i){
//     document.write(i + "<br>")
//     i--
// }


// let n, res = 1;
// do{
//     n = +prompt("Введите число: ", 10);
//     if(n == 0){
//         break;
//     }
//     res *= n;
// }while (true);
// document.write("Произведение: " + res)


// let i = 1;
// do{
//     document.write(i + " ");
//     if(i == 5){
//         break;
//     }
//     if(i == 3){
//         i++;
//         continue;
//     }
//     i++
//     document.write(i + " ")
// }while (true);




// for (let i = 0; i < 5; i++) {
//     document.write(i + " ")
// }




let start = 5;
let end = 18; 
let sum = 0;
let res = 1;
let count = 0;

for(let i = start; i <= end; i++){  // 5 6 7 8 9 10
    if(i>8){
        count++;
    }
    if(i%2==0){
        sum += i; // sum = 0 + 6 + 8 + 10
    }
    else{
        res *= i; // res = 1 * 5 * 7 * 9
    }
}
document.write(`Сумма чётных чисел: ${sum}<br>Произведение нечётных чисел: ${res}<br>Количество чисел больше 8: ${count}`)
