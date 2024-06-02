"use strict";

// let element = document.querySelector("#root");
// console.log(element);

// let tag = document.createElement("p"); // tag = <></>
// let node = document.createTextNode("Новый текст"); // node = новый текст

// tag.append(node);

// element.append(tag); // добавляет в род.класс последним
// element.prepend(tag); // добавляет в род.класс первым
// element.before(tag); // до род.класса
// element.after(tag); // после род.класса
// element.replaceWith(tag); // заменяет на новый элемент выбранный id



// let list = document.querySelector("ul");
// let newItem = document.createElement("li");

// newItem.innerHTML = ("Новый <i>Теееекст</i>")
// list.append(newItem)



// let i = 1;

// document.querySelector("#func1").addEventListener("click", changeItem);
// document.querySelector("#func2").addEventListener("click", addItem);

// function changeItem(){
//     let element = document.querySelector("#list2").lastChild;
//     document.querySelector("#list1").append(element)
// }

// function addItem(){
//     let element = document.createElement("li");
//     element.innerHTML = ("Water" + i);
//     document.querySelector("#list2").append(element);
//     i++
// }



// let div = document.querySelector("#root");
// div.insertAdjacentHTML("beforebegin", "<p>До выбранного элемента</p>");
// div.insertAdjacentHTML("afterend", "<p>После выбранного элемента</p>");
// div.insertAdjacentHTML("afterbegin", "<p>Внутри первым выбранного элемента</p>");
// div.insertAdjacentHTML("beforeend", "<p>Внутри последним выбранного элемента</p>");

// let first = document.querySelector("#p1");
// // first.remove();
// let second = document.querySelector("#p2");
// second.after(first)


// let ul = document.querySelector("ul");
// let li = ul.cloneNode(true);
// console.log(li);

// li.querySelector("li").innerHTML = "Начало клонируемых элементов"
// ul.after(li)


let list = document.querySelector(".list");
list.insertAdjacentHTML("beforebegin", "<h2>Список</h2><hr>");
let list_inner = document.querySelector("h2");
list_inner.insertAdjacentText("beforeend", " планет");
list.insertAdjacentHTML("afterend", "<hr>");

let hr = document.querySelectorAll("hr")[1];
let h4 = document.createElement("h4");
h4.innerHTML = "Конец списка";
hr.insertAdjacentElement("afterend", h4);

let idRemove = setInterval(function (){
    let li = document.querySelector("ul li");
    if(li == null){
        clearInterval(idRemove);
        // alert("Список удален")
        list.insertAdjacentHTML("afterbegin", "<li>Список удален</li>")
    }else{
        li.remove()
    }
}, 1000)
