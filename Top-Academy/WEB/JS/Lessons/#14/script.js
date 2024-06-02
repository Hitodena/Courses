"use strict";

// function Car(name, year){
//     this.name = name
//     this.year = year
//     this.getAge = function(){
//     return new Date().getFullYear() - this.year
// }
// }

// let dodge = new Car("Dodge", 1969)
// let nissan = new Car("Nissan", 2002)

// Car.prototype.getAge = function(){
//     return new Date().getFullYear() - this.year
// }

// class User{

//     constructor(name){
//         this.name = name
//     }

//     sayHi(){
//         document.write(`Hello ${this.name}!`)
//     }
// }

// let user = new User("фы")
// user.sayHi()

// class Header{
//     constructor(img, h1, h2){
//         this.scr = img
//         this.h1 = h1
//         this.h2 = h2
//         this.out = ""
//     }
//     render(id){
//         this.out = `
//         <img src="${this.scr}">
//         <h1>${this.h1}</h1>
//         <h2>${this.h2}</h2>
//         `
//         document.querySelector(`#${id}`).innerHTML = this.out;
//     }
// }

// class HeaderExt extends Header{ // дочерний
//     constructor(img, h1, h2, tel){
//         super(img, h1, h2);
//         this.tel = tel
//     }
//     get tel(){
//         return this._tel
//     }
//     set tel(t){
//         let reg = /^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?$/;
//         if (reg.test(t)){
//             this._tel = t
//         }else{
//             alert("Неккоректный номер телефона")
//             return
//         }
//     }
//     render(id){
//         super.render(id)
//         this.out += `
//         ${this.tel}
//         `
//         document.querySelector(`#${id}`).innerHTML = this.out
//     }
// }

// let img = "1.jpg"
// let head = new Header(img, "Заголовок", "Описание")
// head.render("header1")

// let img2 = "1.jpg"
// let head2 = new Header(img, "Заголовок 2", "Описание 2")
// head2.render("header2")

// let img3 = "1.jpg"
// let head3 = new HeaderExt(img, "Дочерний класс", "Описание 3", "+7987654332")
// head3.tel = "hello"
// head3.render("head-ext")

// // json

// let info = '{"first_name":"Ivan","age":36,"mother":{"name":"Olga","age":58},"children":["Kate","Igor","Misha"],"married":true,"dog":null}'

// // JSON.parse() // json => object
// // JSON.stringify() // object => json

// let person = JSON.parse(info)
// console.log(person)

// person.first_name = "Lexa"
// delete(person.age)
// console.log(person)

// person.work = "js react"
// console.log(person)

// let personStr = JSON.stringify(person)
// console.log(personStr)

// fetch('https://jsonplaceholder.typicode.com/todos')
//       .then(response => response.json())
//       .then(json => console.log(json))

// ajax

document.querySelector("#load").addEventListener("click", load);

function load() {
    let url = "https://jsonplaceholder.typicode.com/users";
    fetch(url)
        .then(function (response) {
            return response.json()
        })
        .then(function (data) {
            let ul = document.querySelector("#list")
            let html = data.map(function (item) {
                return `<li>${item.id} ${item.name} ${item.email}</li>`
            })
            ul.insertAdjacentHTML("afterbegin", html.join(" "))
        })
}
