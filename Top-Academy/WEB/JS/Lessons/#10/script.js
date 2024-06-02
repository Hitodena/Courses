"use strict";

// document.write("<div id='text'>Здесь будет отображаться текущее время</div>");

// window.addEventListener("load", function(){
//     setInterval(time, 1000);
// });

// function time(){
//     let d = new Date();
//     let hour = d.getHours();
//     let min = d.getMinutes();
//     let sec = d.getSeconds();
//     if(sec < 10){
//         sec = "0" + sec
//     }
//     let time = hour + ":" + min + ":" + sec;
//     document.querySelector("#text").innerHTML = time
// }

// let a = document.querySelector("#cl");
// a.addEventListener("click", move);

// function move(){
//     // a.style.display = "none"
//     a.style.visibility = "hidden"
//     let smsq = document.querySelector("#animate");
//     let pos = 0;
//     let id = setInterval(frame, 5);
//     function frame(){
//         if(pos == 350){
//             // a.style.display = "block"
//             a.style.visibility = "visible"
//             clearInterval(id)
//         }else{
//             pos++;
//             smsq.style.top = pos + "px";
//             smsq.style.left = pos + "px";
//         }
//     }
// }



// let img = document.querySelector("img");
// img.border = 1;

// document.write(`<br>Ширина изображения: ${img.width}px`)
// document.write(`<br>Высота изображения: ${img.height}px`)
// img.src = "blue_star.png";
// img.width = 128
// img.height = 128


// let img = document.querySelector("img");
// img.addEventListener("click", changeImage);

// let flag = 0;
// function changeImage(){
//     if (flag == 0){
//         img.src = "blue_star.png"
//         flag = 1
//     }else{
//         img.src = "golden_star.png"
//         flag = 0
//     }
// } 




// let array = new Array('JS_7/2.jpg', 'JS_7/3.jpg', 'JS_7/4.jpg');
// document.write("<input type='button' value='<' name='left'>");
// document.write("<img id='sl' src='"+ array[0] +"'>");
// document.write("<input type='button' value='>' name='right'>");
   
// let lt = document.getElementsByName('left')[0];
// let rt = document.getElementsByName('right')[0];
// rt.addEventListener("click", getRight);
// lt.addEventListener("click", getLeft);
 
// let i = 0;
// let image = document.getElementById("sl");
 
// function getRight(){
//     i++;
//     if(i == array.length){
//         // i=0;
//         i--;
//         // rt.disabled = "true";
//         rt.style.visibility="hidden";
//     }
//     if(i == 1){
//         lt.style.visibility="visible";
//     }
   
//     console.log(i);
//     image.src = array[i];
// }
 
// function getLeft(){
//     i--;
//     if(i < 0){
//         // i = array.length - 1;
//         i++;
//         lt.style.visibility="hidden";
//     }
//     if(i == array.length - 2){
//         // rt.disabled = "false";
//         rt.style.visibility="visible";
//     }
//     console.log(i);
//     image.src = array[i];
// }


let title = document.querySelector("h1").firstChild.nodeValue;
console.log(title);

let d = document.querySelector(".one");
if(d.nodeName == "DIV"){
    d.innerHTML = "Wassup"
}
