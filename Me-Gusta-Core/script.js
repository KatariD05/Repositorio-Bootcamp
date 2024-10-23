document.addEventListener('DOMContentLoaded', function(){
    let buttons = document.querySelectorAll(".btn");
    let counters = document.querySelectorAll(".counter");

    buttons.forEach((button, index) =>{
        button.addEventListener("click", function (){
            let currentCounter = counters[index];
            let count = currentCounter.innerText;
            count++;
            currentCounter.innerText = count;
        });
    });
});