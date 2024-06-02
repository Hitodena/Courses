"use script";


// let gas = document.querySelectorAll(".petrol");
// let res

// for (let index = 0; index < gas.length; index++){
//     gas[index].addEventListener("click", function(){
//         let amount = gas[index].getAttribute("data-set")
//         let gallons = document.querySelector(".gallons").value
        
//         res = amount * gallons
//         let sum = document.querySelector(".sum")
//         sum.innerHTML = res
//     })
    
// }



// let array = [1, 2, 3, 4, 5]

// console.log(typeof(array))





// let menu = {
//     "width-menu": 300,
//     heightmenu: 200,
//     title: "menu"
// }
// console.log(menu)
// document.write(menu.title + ": " + menu["width-menu"] + "x" + menu.heightmenu)




// let car = new Object();
// car["type"] = "Dodge"
// car.model = "Charger"
// car["year"] = 1969

// // delete car.model

// delete(car.model)
// car.version = "r/t"

// for(let i in car){
//     document.write("<br>Ключ: " + i + ", значение: " + car[i])
// }

// document.write("<br>", Object.keys(car))
// document.write("<br>", Object.keys(car).length)



// Object.keys(car).forEach(function(key){
//     document.write("<br>" + key + ": " + car[key])
// })

// Object.keys(car).forEach(key => document.write("<br>" + key + ": " + car[key]))



// let obj = {
//     name: "Гомер",
//     colors: {
//         first: "yellow",
//         second: "blue"
//     },
//     color: [
//         "black",
//         "white",
//         "red",
//         "blue"
//     ],
//     hello: function(){
//         document.write("Привет")
//     }
// }

// // console.log(obj)
// // document.write(obj.name + " " + obj.color[1] + " " + obj.colors.second + "<br>")
// // obj.hello()


// // let fill = obj.color.filter(function(elem){
// //     return elem.length < 5
// // })
// // document.write(fill + "<br>")




// // let mas = obj.color.map(elem => elem.toUpperCase())
// // let mas = obj.color.map(function(elem, index, all){
// //     return index + ": " + elem + " " +  all + "<br>"
// // })

// mas = Object.keys(obj.colors).map(elem => elem.toUpperCase())


// document.write(mas + "<br>")
// console.log(mas)




// let calc = {
//     num1: 5,
//     num2: 2,
//     calculate: function(){
//         // this.res = this.num1 * this.num2;
//         calc.res = calc.num1 * calc.num2
//     }
// }


// calc.calculate();
// document.write(calc.res)





let x = 15
let y = 10

// let cords = {
//     x: x,
//     y: y,
//     calc: function(){
//         document.write(this.x * this.y)
//     }
// }

// let cords = {
//     x,
//     y,
//     calc(){
//         document.write(this.x * this.y)
//     }
// }

// cords.calc()



// let user = {
//     login: {
//         firstName: "kate",
//         lastName: "pavlova"
//     },
//     password: "qwerty",
//     role: "guest"
// }

// let log = user.login;
// let {login:{firstName: f, lastName}, ...rest} = user
// document.write(`${f} ${rest.password} ${rest.role}`)



// let number = [3, 5, 6];
// let [a, b, c] = number;

// document.write(a, b, c)