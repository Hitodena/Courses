"use strict";
let end = 30;
let answer = 1;
for(let start = 10; start < end; start++){
    if (start % 2 != 0){
        let multiply = answer;
        answer *= start;
        document.write(`${start} x ${multiply} = ${answer}<br>`)
    }
}

let med = 0
let list = [];
for (let index = -1; index < list.length; index++) {
    let number = Number(prompt("Введите число (0 - выход):"));
    if(number == 0){
        let sum = list.reduce((sum, current) => sum + current, 0);
        let length = list.length;
        med = (sum / length);
        document.write(`Количество чисел : ${length}<br>Сумма чисел: ${sum}<br>Среднее арифметическое: ${med} `)
        break;
    }
    list.push(number);
}
