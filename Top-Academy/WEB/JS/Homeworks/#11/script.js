"use strict";

let spans = document.querySelectorAll("span")

for(let i = 0; i < spans.length; i++){
    spans[i].addEventListener("click", function(){
        spans[i].parentNode.remove();
    })
}
