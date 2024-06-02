"use strict";
let login = prompt("Введите логин: ", "admin")
if(login){
    if(login == "admin"){
        let pass = prompt("Введите пароль: ")
        if(pass){
            if(pass){
                if(pass == "password"){
                    alert("Добро пожаловать!")
                }
                else{
                    alert("Пароль неверный")
                }
            }

        }
        else{
            alert("Вход отменён")
        }
    }
    else{
        alert("Я вас не знаю")
    }
}

else{
    alert("Вход отменён")
}