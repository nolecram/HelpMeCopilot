// Step 1: Create a basic structure for the JavaScript program
function fahrenheitToCelsius(fahrenheit) {
    return (fahrenheit - 32) * 5 / 9;
}

// Step 2: Implement input and output functionality
// Read an input value for Fahrenheit
const fahrenheitInput = prompt("Enter temperature in Fahrenheit:");

// Convert the input value to a number
const fahrenheit = parseFloat(fahrenheitInput);

// Check if the input is a valid number
if (isNaN(fahrenheit)) {
    alert("Please enter a valid number.");
} else {
    // Call the function and store the result
    const celsius = fahrenheitToCelsius(fahrenheit);

    // Display the converted Celsius value
    alert(`Temperature in Celsius: ${celsius.toFixed(2)}`);
}
