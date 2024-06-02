"use strict";


let t = document.querySelectorAll("#clock img");

let imgTime = ["c0.gif", "c1.gif", "c2.gif", "c3.gif", "c4.gif", "c5.gif", "c6.gif", "c7.gif", "c8.gif", "c9.gif", ];

clock()

function clock(){
    let time = new Date();
    let hours = time.getHours();
    let minutes = time.getMinutes();
    let seconds = time.getSeconds(); 
    getImg(hours, minutes, seconds)
    setTimeout(clock, 1000);
}

function getImg(h, m, s){
    t[0].src = imgTime[Math.floor(h/10)]
    t[1].src = imgTime[h%10]

    t[3].src = imgTime[Math.floor(m/10)]
    t[4].src = imgTime[m%10]
    
    t[6].src = imgTime[Math.floor(s/10)]
    t[7].src = imgTime[s%10]
}