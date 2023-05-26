function sum(num) {
    if(num > 0) {
        return num + sum(num - 1);
    }
    else {
        return num;
    }
 }

 // Build a test for the previous function
    // Test the function with a positive integer


const number = parseInt(prompt('Enter a positive integer: '));

const result = sum(number);

console.log(`The sum is ${result}`);

function addRange(num) {
    if(num > 0) {
        return num + addRange(num - 1);
    }
    else {
        return num;
    }
 }
 function addRandomNumbers(num) {
    if(num > 0) {
        return num + addRandomNumbers(num - 1);
    }
    else {
        return num;
    }
 }
 function async