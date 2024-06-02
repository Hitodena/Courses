"use strict";

let numberMonth = Number(prompt("Введите номер месяца по счёту:"));

switch(numberMonth){
    case 1:
        alert("Количество дней: 31")
        break;
    case 2:
        let year = Number(prompt("Введите год:"));
        if(year %4 == 0){
            alert("Количество дней: 29")
        }
        else{
            alert("Количество дней: 28")
        }
        break;
    case 3:
        alert("Количество дней: 31");
        break;
    case 4:
        alert("Количество дней: 30");
        break;
    case 5:
        alert("Количество дней: 31");
        break;
    case 6:
        alert("Количество дней: 30");
        break;
    case 7:
        alert("Количество дней: 31");
        break;
    case 8:
        alert("Количество дней: 31");
        break;
    case 9:
        alert("Количество дней: 30");
        break;
    case 10:
        alert("Количество дней: 31");
        break;
    case 11:
        alert("Количество дней: 30");
        break;
    case 12:
        alert("Количество дней: 31");
        break;
    default:
        alert("Неккоректный ввод данных");
}