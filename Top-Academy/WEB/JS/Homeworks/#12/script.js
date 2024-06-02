"use strict";

let choose = document.querySelector("input[type='button']");
choose.addEventListener("click", () =>{
    let answer = document.form.radio.value;
    let field = document.querySelector("#answer")
    field.textContent = (`Ответ: ${answer}`)
})