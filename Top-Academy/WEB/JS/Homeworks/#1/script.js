"use strict";
// 1)
let path = "D:\\projects\\script.js"
alert("Инструкция:\nДокумент script.js лежит в папке " + path)
// 2)
let animal = prompt("Какое ваше любимое животное?") 
let meat = prompt("Чем оно питается?")
let exercise = prompt("Какое ваше любимое упражнение в спорте?")
let weight = prompt("Какой рабочий вес в этом упражнении?")
let rep = prompt("Сколько вы делаете подходов?")
alert("Ваш(-а, -е) " + animal + " " + "питается " + meat + " " + "и " + "делает " + exercise + " " + "с рабочим весом " + weight + " " + "на " + rep + " " + "подходов.")
// 3)
let fname = prompt("Введите ваше имя")
let sname = prompt("Введите вашу фамилию")
let city = prompt("Где вы проживаете?")
let age = prompt("Сколько вам лет?")
let res = confirm(`Вас зовут ${fname} ${sname}\nВаше место проживания: ${city}\nВаш возраст: ${age}\nВсё верно?`)
if (res) {
    alert("Благодарим за предоставленную информацию.")
}
else{
    alert("Попробуйте заново.")
}