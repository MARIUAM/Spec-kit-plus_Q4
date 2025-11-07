const billInput = document.getElementById('bill');
const tipButtons = document.querySelectorAll('.tip-btn');
const customTipInput = document.getElementById('custom-tip');
const peopleInput = document.getElementById('people');
const tipAmountDisplay = document.getElementById('tip-amount');
const totalAmountDisplay = document.getElementById('total-amount');
const resetBtn = document.getElementById('reset-btn');

let bill = 0;
let tipPercentage = 0;
let numberOfPeople = 1;

function calculateTip() {
    if (bill >= 0 && tipPercentage >= 0 && numberOfPeople > 0) {
        const tipAmount = (bill * tipPercentage) / 100;
        const totalAmount = bill + tipAmount;
        const tipAmountPerPerson = tipAmount / numberOfPeople;
        const totalAmountPerPerson = totalAmount / numberOfPeople;

        tipAmountDisplay.textContent = `$${tipAmountPerPerson.toFixed(2)}`;
        totalAmountDisplay.textContent = `$${totalAmountPerPerson.toFixed(2)}`;
    } else {
        tipAmountDisplay.textContent = '$0.00';
        totalAmountDisplay.textContent = '$0.00';
    }
}

function handleBillInput() {
    bill = parseFloat(billInput.value) || 0;
    calculateTip();
}

function handleTipButtonClick(event) {
    tipPercentage = parseFloat(event.target.textContent) || 0;
    customTipInput.value = '';
    calculateTip();
}

function handleCustomTipInput() {
    tipPercentage = parseFloat(customTipInput.value) || 0;
    calculateTip();
}

function handlePeopleInput() {
    numberOfPeople = parseInt(peopleInput.value) || 1;
    if (numberOfPeople === 0) {
        peopleInput.value = 1;
        numberOfPeople = 1;
    }
    calculateTip();
}

function resetCalculator() {
    bill = 0;
    tipPercentage = 0;
    numberOfPeople = 1;

    billInput.value = '';
    customTipInput.value = '';
    peopleInput.value = '1';

    calculateTip();
}

billInput.addEventListener('input', handleBillInput);
customTipInput.addEventListener('input', handleCustomTipInput);
peopleInput.addEventListener('input', handlePeopleInput);
resetBtn.addEventListener('click', resetCalculator);

tipButtons.forEach(button => {
    button.addEventListener('click', handleTipButtonClick);
});
