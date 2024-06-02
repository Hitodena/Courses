"use strict";

// function change(id){
//     id.innerHTML = "Новый текст"
// }

// function setColor(a){
//     document.body.style.background = a.className
// }

// let button = document.querySelector("#button")

// button.onclick = function(){
//     alert("Спасибо")
// }

// button.onclick = hello;

// function hello(){
//     alert("Спасибо")
// }

// let button = document.querySelector("#button")
// button.addEventListener("click", function(){
//     button.innerHTML = "Новый текст"
// })

// button.addEventListener("contextmenu", setColor)
// function setColor(){
//     button.style.color = "green"
//     button.style.background = "yellow"
// }

// document.addEventListener("mousemove", function(a){
//     let c = document.querySelector("#ev")
//     let x = a.clientX
//     let y = a.clientY

//     c.textContent = `X = ${x}, Y = ${y}`

//     c.addEventListener("dblclick", function(event){
//         event.target.style.background = "darkred"
//     })
// })

// let button = document.querySelector("#button")

// button.addEventListener("click", hello)

// function hello(){
//     alert("hello")
//     button.removeEventListener("click", hello)
// }

// setTimeout("alert('Текст')", 1295);

// document.write("<div id='dt'>Создание анимированного текста</div>");
// let id = document.querySelector("#dt");
// let text = document.querySelector("#dt").innerHTML;
// let i = 0;
// let time;

// window.addEventListener("load", animText);

// function animText(){
//     id.innerHTML = text.substring(0, i);
//     i++;
//     if(i == 31){
//         i = 0;
//         // clearTimeout(time);
//     }
//     // console.log(i)
//     time = setTimeout(animText, 105);
//     // console.log(time)
// }

// let date = new Date()
// document.write(date.toDateString(), "<br>")
// document.write(date.getFullYear(), "<br>")
// document.write(date.getMonth(), "<br>")
// document.write(date.getDate(), "<br>")
// document.write(date.getDay(), "<br>")

// let months = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"];

// let days = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

// let date = new Date();
// let fullDate  = `Сегодня: ${date.getDate()} ${months[date.getMonth()]} ${date.getFullYear()} года, ${days[date.getDay()]} `;
// document.write(fullDate);


// setInterval(setColor, 1000)

// function setColor(){
//     let x = document.body;
//     x.style.background = (x.style.background == "yellow") ? "orange" : "yellow";
// }



document.write("<input type='button' value='Start / Stop'>")
document.querySelector("input").addEventListener("click", st)

function setColor(){
    let x = document.body;
    x.style.background = (x.style.background == "yellow") ? "orange" : "yellow";
}

let act, run;
function st(){
    if(!run){
        act = setInterval(setColor, 1000);
    }
    else{
        clearInterval(act)
    }
    run = !run;
}