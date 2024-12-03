
// Function to display a greeting message
function displayGreeting() {
    alert("Welcome to the Hello World program!");
}

// Call the greeting function
displayGreeting();

// Function to convert hours to seconds
function hoursToSeconds(hours) {
    return hours * 3600;
}

// Implement input and output functionality
// Read an input value for hours
const hoursInput = prompt("Enter time in hours:");

// Convert the input value to a number
const hours = parseFloat(hoursInput);

// Check if the input is a valid number
if (isNaN(hours)) {
    alert("Please enter a valid number.");
} else {
    // Call the function and store the result
    const seconds = hoursToSeconds(hours);

    // Display the converted seconds value
    alert(`Time in seconds: ${seconds}`);
}
