"use strict";
let daynumb = prompt("Введите день недели(цифрами): ");
let day = null;
if (daynumb == 1) {
    day = "Понедельник";
} else if (daynumb == 2) {
    day = "Вторник";
} else if (daynumb == 3) {
    day = "Среда"
} else if (daynumb == 4) {
    day = "Четверг"
} else if (daynumb == 5) {
    day = "Пятница"
} else if (daynumb == 6) {
    day = "Суббота"
} else if (daynumb == 7) {
    day = "Воскресенье"
} else{
    day = "Неккоректное значение"
}

alert(`День недели - ${day}`)


