// let a = 5
// if(!a){    // && - and ! - not || - or
//     alert("True")
// }
// else{
//     alert("False")
// }

// alert(!10) // !10 == false => negative false => true




// let age = prompt("Введите возраст:")
// if(age < 18 || age > 69){
//     alert("Вы не можете получить права")
// }
// else{
//     alert("Вы можете получить права")
// }



// switch(переменная){
//     case значение 1:
//         код
//     break
//     case значение 2:
//         код 
//     break
//     default:
//         код
// }


// let a = +prompt("Введите результат '2 x 2' ")
// switch(a - 1){
//     case 4: alert("Верно"); break
//     case 3: ; case 5: alert("Не верно") ; break
//     default: alert("Такого не знаю")
// }



// let m = +prompt("Введите номер месяца: ")
// let n = null
// switch (m){
//     case 1: n = "Январь"; break
//     case 2: n = "Февраль"; break
//     case 3: n = "Апрель"; break
//     case 4: n = "Март"; break
//     case 5: n = "Май"; break
//     case 6: n = "Июнь"; break
//     case 7: n = "Июль"; break
//     case 8: n = "Август"; break
//     case 9: n = "Сентябрь"; break
//     case 10: n = "Октябрь"; break
//     case 11: n = "Ноябрь"; break
//     case 12: n = "Декабрь"; break
//     default: n = "Нет такого"
// }
// alert(n)


// let a = parseInt(prompt("Введите число: "))  
// let b = parseInt(prompt("Введите число: "))
// let operator = (prompt("Выберите действие: (+, -, /, *)"))

// switch (operator){
//     case "+": let sum = a + b; alert("Сумма: " + sum); break;
//     case "-": let sub = a - b; alert("Разность: " + sub); break;
//     case "/": let div = a / b; alert("Частность: " + div); break;
//     case "*": let mul = a * b; alert("Произведение: " + mul); break;
//     default: alert("Нету такого") ;break;
// }



// document.write("<img src='1.jpg'>")








// do {
//     code
// } while (condition);

let i = 5
do {
    document.write("Чпоньк: " + i + "<br>")
    i = --i
} while (i > 0);








