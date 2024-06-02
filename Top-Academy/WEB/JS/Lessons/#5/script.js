// for(let i=0; i<4; i++){
//     document.write("+++" + i + "<br>")
//     for(let j=0; j<2; j++){
//         document.write("--" + j + "<br>")
//     }
// }

// let symbol = prompt("Введите символ: ")
// let tr = prompt("Введите кол-во строк: ")
// let td = prompt("Введите кол-во столбцов: ")
// document.write('<table border="1">');
// for(let i = 0; i < tr; i++){
//     document.write("<tr>");
//     for(let j = 0; j < td; j++){
//         document.write("<td>" + symbol + "</td>");
//     }
//     document.write("</tr>");
// }
// document.write("</table>");


// document.write('<table border="1" width="300">');
// for(let i = 1; i <= 10; i++){
//     document.write("<tr align='center'>");
//     for(let j = 1; j <= 10; j++){
//         if(i%2 == 0){
//             document.write("<td bgcolor=red>" + j * i + "</td>")
//         }
//         else{
//             document.write("<td bgcolor=yellow>" + j * i + "</td>");
//         } 
//     }
//     document.write("</tr>");
// }
// document.write("</table>");


// let arr = [2, 6, 8];
// arr[2] = 10;
// arr[12] = 100;
// document.write(arr[12]);
// console.log(arr);

// let arr1 = new Array(2, 6, 8);
// console.log(arr1);
// console.log(typeof(arr1));

// let arr2 = [5];
// let arr3 = new Array(5);
// console.log(arr2)
// console.log(arr3)



// let f = [1, 2, 3, 4, 5, 6];
// document.write(f + "<br>");
// document.write(f.length + "<br>");
// f.length = 3
// document.write(f + "<br>")
// f.length = 6
// document.write(f + "<br>")



// let array = [5, 9, -3, -1, 4, -8, 7, 2, -6]
// console.log(array)
// for (let index = 0; index < array.length; index++){
//     if(array[index] < 0){
//         array[index] *= -1
//     }
//     document.write(index + ': ' + array[index]*2 + "<br>")
// }


// let array = [5, 9, -3, -1, 4, -8, 7, 2, -6]
// let sum = 0
// for (let index = 0; index < array.length; index++){
//     if (array[index] < 0){
//         sum += array[index]
//     }
// }
//     document.write(sum)


// let array = new Array(5);
// for (let index = 0; index < array.length; index++){
//     array[index] = prompt(`Введите ${index + 1} элемент массива`)
// }
// document.write(array + "<br>"); 


// for(let index=array.length-1; index >= 0; index-- ){
//     document.write(array[index] + " ")
// }


// let array = [2, 7, 8, "оаоаоаа", 1.5, true]
// console.log(array)

// let array = [[2, 1, 1], [6, 3, 7], [8, 5, 6]];
// console.log(array)
// console.table(array);
// document.write(array[1][2])



let questions = ["На ноль делить можно?", "Волга впадает в Каспийское море?", "Атмосферное давление увеличивается с высотой", "2x2 будет 8", "Дельфины - это рыбы", "Мадонна - это настоящее имя певицы", "Первая мировая война началась 1 сентября 1939 года"];  
let answers = [false, true, false, false, false, false, false];
let res = new Array()
let sum = 0
for(let index = 0; index < questions.length; index++){
    let answer = confirm(questions[index]);
    if (answer == answers[index]){
        res[index] = 10
    }
    else{
        res[index] = 0
    }
    sum += res[index]
}
document.write("<table border='1'>");
document.write("<tr>");
document.write("<th>Вопрос</th>");
document.write("<th>Баллы</th>");
document.write("</tr>");

for(let index = 0; index < questions.length; index++){
    document.write("<tr>");
    document.write("<td>" + questions[index] + "</td>");
    document.write("<td>" + res[index] + "</td>");
    document.write("</tr>");
}

document.write("<tr>");
document.write("<th>Итого</th>");
document.write("<th>" + sum + "</th>");
document.write("</tr>");
document.write("</table>");




