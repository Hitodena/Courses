"use strict";

let months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

let createColor = () => Math.floor(Math.random() * 256)

for (let index = 0; index < months.length; index++) {
    document.write(`<div id=${index}>${months[index]}</div>`);
    let id = document.getElementById(index)
    id.style.height = "20px"
    id.style.width = "95%"
    id.style.margin = "20px"
    id.style.fontWeight = "900"
    id.style.padding = "20px"
    id.style.textAlign = "center"
    id.style.backgroundColor = `rgb(${createColor()}, ${createColor()}, ${createColor()})`
}
