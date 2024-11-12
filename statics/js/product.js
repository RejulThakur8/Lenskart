// const minus = document.querySelector(".subtraction"),
//     num = document.querySelector(".num"),
//     plus = document.querySelector(".addition");

//     let a = 0;

// plus.addEventListener('click', ()=>{
//     a++;
//     a = (a < 10) ? + a : a;
//     num.innerHTML = a;
// });

// minus.addEventListener('click', ()=>{
//     if(a > 1){
//         a--;
//         a = (a < 10) ? + a : a;
//         num.innerHTML = a;
//     }
// })


const subtract = document.querySelector(".subtraction"),
 number = document.querySelector(".num"),
 add = document.querySelector(".addition");

let a = 1;

subtract.addEventListener('click', ()=>{
    if(a > 1){
        a--;
        a = (a < 10) ? + a : a;
        number.innerHTML = a;
    }
});

add.addEventListener('click', ()=>{
    a++;
    a = (a < 10) ?  + a : a;
    number.innerHTML = a;
});