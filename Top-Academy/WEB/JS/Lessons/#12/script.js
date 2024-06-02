"use strict";

// let div = document.querySelector("div");
// div.className = ("alert");
// let divActive = document.querySelector(".active");
// divActive.classList.add("hidden");
// // divActive.classList.remove("hidden");
// divActive.classList.toggle("hidden");
// divActive.classList.replace("active", "alert");


// let frog = document.querySelector("#greenfrog");

// console.log(frog)
// console.log(frog.alt)
// console.log(frog.className)
// console.log(frog.id)
// console.log(frog.title)
// console.log(frog.src)
// console.log(frog.getAttribute("src"))
// console.log(frog.getAttribute("data-frog"))
// console.log(frog.setAttribute("src", "c0.gif"))






// document.form1.style.background = ("darkred");

// document.forms[0].style.margin = ("20px");
// document.forms["form1"].style.padding = ("16px");
// document.forms.form1.style.border = ("2px solid black");
// document.forms.form1.style.borderRadius = ("15px");
// document.forms.form1.style.width = ("37%");
// document.forms.form1.style.margin = ("0 auto");
// document.forms.form1.style.marginTop = ("30vh");


// document.form1.name1.style.color = ("darkred");
// document.form1.name1.style.borderRadius = ("15px");
// document.form1.name1.style.border = ("none");
// document.form1.name1.style.padding = ("10px");
// document.form1.name1.style.background = ("lightgray");


// let button = document.querySelector("#button");
// let input = document.querySelector("#text1")

// button.addEventListener("click", () => {
//     alert(input.value)
// })


let choose = document.querySelector("input[type='button']");
choose.addEventListener("click", chooseColor);

function chooseColor(){
    document.form3.style.background = document.form3.radio2.value
}

