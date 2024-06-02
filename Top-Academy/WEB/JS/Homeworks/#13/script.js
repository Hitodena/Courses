"use strict";


let cars = ['Ferrari', 'Lamborghini', 'Porsche', 'Tesla', 'BMW', 'Audi', 'Mercedes'];

function lottery(name) {
    let randomCarIndex = Math.floor(Math.random() * cars.length);
    let randomCar = cars[randomCarIndex];
    alert(`${name}, вы выйграли автомобиль: ${randomCar}`);
}

let userName = prompt('Введите ваше имя:');
lottery(userName);