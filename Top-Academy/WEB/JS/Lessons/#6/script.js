// document.write('<table border="1" width="300">');
// for(let i = 1; i <= 10; i++){
//     document.write("<tr align='center'>");
//     for(let j = 1; j <= 10; j++){
//         if((i+j) % 2){
//             document.write("<td bgcolor=red>" + j * i + "</td>")
//         }
//         else{
//             document.write("<td bgcolor=yellow>" + j * i + "</td>");
//         } 
//     }
//     document.write("</tr>");
// }
// document.write("</table>");



// let text1 = document.getElementById("text1");
// console.log(text1);
// console.log(text1.textContent);
// text1.textContent = "Новое <b>содержимое</b>";
// let text2 = document.getElementById("text2");
// text2.innerHTML = "Новое содержимое <b>с html разметкой</b>"


// res = prompt("Выберите изображение(1 - собака, 2 - кот, 3 - птица, 4 - рыба)")
// document.write("<div id='image'></div>")
// let img = document.getElementById("image")
// switch (res){
//     case "1":
//         img.innerHTML = "<img src='img/dog.jpg'>" 
//         break;
//     case "2":
//         img.innerHTML = "<img src='img/cat.jpg'>" 
//         break;
//     case "3":
//         img.innerHTML = "<img src='img/bird.jpeg'>" 
//         break;
//     case "4":
//         img.innerHTML = "<img src='img/fish.jpeg'>" 
//         break;
//     default:
//         alert("Вы выбрали не то!");
// }



// let tag = document.getElementsByTagName("p")[2];
// console.log(tag);
// tag.innerHTML = "Hello Tag";
// tag.style.color = "DarkRed"
// tag.style.fontWeight = "Bold" 
// tag.style.backgroundColor = "Magenta"
// tag.style.padding = "10px 20px"

// // list-style-type => listStyleType


// tag.id = "test"
// tag.className = "x"


// let element = document.getElementsByClassName("two")
// console.log(element)
// element[0].style.color = "aqua"
// element[1].style.color = "aquamarine"


/*
document.querySelectorAll(css)
document.querySelector(css)
*/



// let el = document.querySelector("h2")
// // alert(el.innerHTML)

// let els = document.querySelectorAll("h2")
// alert(els[0].innerHTML)



// let lists = document.querySelectorAll("li");
// for (let index = 0; index < lists.length; index++) {
//     lists[index].innerHTML += "!!!";
// }

// let purple = document.querySelectorAll(".purple li")
// for (let index = 0; index < purple.length; index++) {
//     purple[index].style.color = "purple"
// }

// let red = document.querySelectorAll(".red li");
// red[1].style.color="red";


// let red = document.getElementsByClassName("red")[0].getElementsByTagName("li")[1];
// red.style.color = "red"


// let h2 = document.getElementById("one");
// h2.style.color = "magenta"



// let js = ["нужно", "учить", "js"]
// console.log(js)

// let a = js.pop()
// console.log(a)

// console.log(js)

// console.log(js.push("js"))
// console.log(js)

// console.log(js.shift())
// console.log(js)

// js.unshift("Почему", "нужно")
// console.log(js)

// let array = js.slice(1, 3)
// js.splice(0, 1)
// console.log(js)

// js.splice(0, 2, "Мы", "изучаем")
// console.log(js)

// js.splice(2, 0, "сложный", "язык")
// console.log(js)

// js.splice(-2, 0, "Но", "очень", "интересный")
// console.log(js)


// let str = js.join(" && ")
// console.log(str)



// let st = ["Фамилия", "Имя", "Отчество"]
// let lst = new Array(3)
// for (let index = 0; index < lst.length; index++){
//     lst[index] = prompt("Введите данные:",  st[index])
// }

// alert(lst.join(" "))


// let users = ["Artem", "Irina", "Sergey", "Boris"]
// document.write(users.sort() + "<br>")

// let n = [1, 5, 15, 2]
// n.sort((a,b)=>a-b)
// document.write(n)


function caption(num){
    for(let index = 1; index <= num; index++){
        document.write("<h" + index + ">Заголовок " + index + "</h" + index + ">");
    }
}

caption(6);
caption(2);
caption(8);