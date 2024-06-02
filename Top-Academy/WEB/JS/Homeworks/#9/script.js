"use strict";

let button = document.querySelector("#click");
button.addEventListener("click", start);
function start(){
    let small = document.querySelector("#small");
    let pos = 0;
    let id = setInterval(frame, 10);
    function frame(){
        if (pos == 350) {
            clearInterval(id);
            button.style.visibility = "visible"
        }
        pos++;
        small.style.left = pos + "px";
        small.style.top = pos + "px";
        if (pos < 350){
            button.style.visibility = "hidden"
        }
    }

}





