// Function to convert hours to seconds
const hoursToSeconds = hours => hours * 3600;

// Implement input and output functionality
// Read an input value for hours
const hoursInput = prompt("Enter time in hours:");

// Convert the input value to a number and check if it's valid
const hours = Number(hoursInput);

if (isNaN(hours)) {
    alert("Please enter a valid number.");
} else {
    // Call the function and store the result
    const seconds = hoursToSeconds(hours);

    // Display the converted seconds value
    alert(`Time in seconds: ${seconds}`);
}

sadkjsajfkhgskldfhkdsahflkdsahfklj
