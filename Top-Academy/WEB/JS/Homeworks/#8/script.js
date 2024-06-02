"use strict";

let img = document.querySelector("#img")
let open = document.querySelector("#open")
let close = document.querySelector("#close")

open.addEventListener("click", () =>{
    img.style.visibility = "visible"
})

close.addEventListener("click", () =>{
    img.style.visibility = "hidden"
})