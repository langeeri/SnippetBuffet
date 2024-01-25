
const decreaseBtn = document.getElementById("decreaseBtn");
const resetBtn = document.getElementById('resetBtn');
const increaseBtn = document.getElementById('increaseBtn');
const countLabel = document.getElementById('countLabel');

let count = 0;

decreaseBtn.onclick = function decrease () {
    count --;
    countLabel.textContent = count;
}

resetBtn.onclick = function reset () {
    count = 0;
    countLabel.textContent = count;
}

increaseBtn.onclick = function increase () {
    count ++;
    countLabel.textContent = count;
}

