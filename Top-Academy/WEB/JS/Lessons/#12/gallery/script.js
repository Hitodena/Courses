"use strict";

let slide = document.querySelectorAll(".slide");

for (let index = 0; index < slide.length; index++) {
    slide[index].addEventListener("click", () => {
        for (let index = 0; index < slide.length; index++) {
            slide[index].classList.remove("active")
        }
        slide[index].classList.add("active")
    });
}

function clear(){
    for(let x = 0; x < slide.length; x++){
        slide[x].classList.remove("active")
    }
}