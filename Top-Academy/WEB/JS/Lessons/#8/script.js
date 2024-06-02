"use strict";

// function hello(name){
//     name = name || "незнакомец";
//     document.write(`Привет, ${name}!<br>`)
// }


// function rectangle(width=200, height=100, background="red"){
//     document.write("<div id='shape'></div>");
//     let sq = document.getElementById("shape");

//     sq.style.width = width + "px";
//     sq.style.height = height + "px";
//     sq.style.background = background;
// }

// rectangle("DarkRed");


// let str = "I\'m a JavaScript programmer.";
// document.write(str + "<br>");
// // document.write(str.length + "<br>");
// // document.write(str[2] + "<br>");
// // str = str[2] + "y";
// // document.write(str + "<br>");
// document.write(str.toLowerCase() + "<br>");
// let l = str.toUpperCase()
// document.write(l);


// let res = prompt("Введите имя:");
// alert(first(res));

// function first(str){
//     let newStr = str[0].toUpperCase();
//     for (let index = 1; index < str.length; index++){
//         newStr += str[index].toLowerCase();
//     }
//     return newStr;
// }



// let email;
// do{
//     email = prompt("Enter email:");
//     if(email.indexOf("@") == -1){
//         alert("Incorrect, again")
//     } else {
//         break
//     }
// }while(true)
// alert("Thanks")



// let str = 'I\'m a JavaScript programmer.';
// let str1 = "Я изучаю JavaScript. Мне нравится JavaScript.";
// str = str.concat(str1);
// document.write(str + "<br><br>")

// document.write(str.slice(0, 3) + "<br>");
// document.write(str.slice(6) + "<br>");
// document.write(str.slice(-24, -10) + "<br>")

// document.write(str.substring(0, 3) + "<br>")
// document.write(str.substring(-24, 7) + "<br>")
// document.write(str.substring(3, 0))

// let py  = str.split("JavaScript")
// console.log(py)

// document.write(py.join("Python"))


function loadStr(){
    alert("Страница была загружена")
}
let m = document.getElementById("mes");
function over(){
    document.getElementById("mes");
    m.style.color = "red";
}
function out(){
    document.getElementById("mes");
    m.style.color = "green";
}
function change(){
    let h2 = document.querySelector("h2");
    h2.style.color = "blue"
}

let createColor = () => Math.floor(Math.random() * 256)

function randomBg(){
    document.body.style.backgroundColor = `rgb(${createColor()}, ${createColor()}, ${createColor()})`
}

let newImg = document.getElementById("new-img")

function on(){
    newImg.src = "night.png"
}
function off(){
    newImg.src = "day.png"
}