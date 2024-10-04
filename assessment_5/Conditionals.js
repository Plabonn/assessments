// Input: Get a number from the user
let number = prompt("Enter a number:");

// Convert the input to a number
number = Number(number);

// Conditional: Check if the number is positive, negative, or zero
if (number > 0) {
    console.log("The number is positive.");
} else if (number < 0) {
    console.log("The number is negative.");
} else {
    console.log("The number is zero.");
}
