# The basic concepts of programming are:

- Input/Output
- Variables/Arrays
- Conditionals
- Loops
- Functions 

### Input: 
Data or information that a system receives, like typing on a keyboard or clicking a mouse.

### Output: 
Data or information that a system sends out, like displaying text on a screen or printing a document.

### Variables:
A variable is a storage space in programming that holds a value, which can change. Think of it as a box with a label that stores data, like a number or a word.
#### Example:
x = 5 (Here, x is a variable holding the value 5.)

### Arrays:
An array is a collection of variables, stored together under one name, that can hold multiple values at once. Each value is accessed by its position (called an index). Think of it as a row of labeled boxes holding different values.
#### Example:
numbers = [1, 2, 3, 4] (This array holds four values: 1, 2, 3, and 4.)

### Conditionals:
 In programming, conditionals are statements that allow a program to make decisions based on certain conditions. They check if something is true or false and then choose what action to take.

#### Example:

- If it's raining, then take an umbrella.

- Else, wear sunglasses.

### Loops: 
In programming, loops are used to repeat a set of instructions until a certain condition is met. They help run the same code multiple times without having to write it repeatedly.

### Functions: 
In programming, a function is a block of code that does a specific job. You can use it whenever you need, instead of repeating the same code.

## All the basic concepts Implemented in C++

### Input/Output:

#### Description of the code:

1. #include <iostream>:
This line includes the input-output stream library, which allows the program to use the cout object for displaying output.

2. using namespace std;:
This line enables the use of elements from the standard namespace (std) without needing to prefix them with std::.

3. int main() { ... }:
This defines the main function, which is where the program starts executing.

4. cout << "Hello World!";:
This line prints the text "Hello World!" to the console. The << operator is used to send the string to the output.

5. return 0;:
This indicates that the program finished successfully. Returning 0 signals no errors occurred.

Output: "Hello World!"

```cpp
#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!";
  return 0;
}
```

### Variables/Arrays:

#### Description of the Code:
1. #include <iostream>:
This line includes the input-output stream library, which allows the use of cout for outputting data.

2. using namespace std;:
This line allows the program to use the standard namespace without needing to prefix standard functions and objects with std::.

3. int main() { ... }:
This defines the main function, where the program starts executing.

4. Variable:

- int age = 25;:
This line declares an integer variable named age and initializes it with the value 25. It stores the age of a person.
- cout << "Age: " << age << endl;:
This outputs the text "Age: " followed by the value of the age variable.

5. Array:

- int scores[5] = {90, 85, 88, 92, 95};:
This line declares an array named scores that can hold 5 integer values. It initializes the array with the scores 90, 85, 88, 92, and 95.
- cout << "Scores: ";:
This outputs the text "Scores: " before printing the array elements.

6. Loop:

- for (int i = 0; i < 5; i++) { ... }:
This loop iterates over the indices of the array from 0 to 4. It accesses each score in the scores array.
- cout << scores[i] << " ";:
Inside the loop, this prints each score followed by a space.

7. return 0;:
This indicates that the program completed successfully.

Output: Age: 25
Scores: 90 85 88 92 95 

```cpp
#include <iostream>
using namespace std;

int main() {
    // Variable
    int age = 25;  // This variable stores the age of a person
    cout << "Age: " << age << endl;

    // Array
    int scores[5] = {90, 85, 88, 92, 95};  // This array stores 5 scores
    cout << "Scores: ";
    
    // Loop through the array to print the scores
    for (int i = 0; i < 5; i++) {
        cout << scores[i] << " ";  // Print each score in the array
    }
    cout << endl;

    return 0;
}
```

### Conditionals:

#### Description of the Code:
1. #include <iostream>:
This line includes the input-output stream library to use cout and cin.
2. using namespace std;:
This allows the program to use elements from the standard namespace without needing the std:: prefix.
3. int main() { ... }:
This defines the main function, where the program execution begins.
4. int number;:
This line declares an integer variable named number to store the user’s input.
5. Input:

- cout << "Enter a number: ";:
This prompts the user to enter a number.
- cin >> number;:
This reads the user's input and stores it in the number variable.
6. Conditional Statements:

- if (number > 0) { ... }:
This checks if the number is greater than zero. If true, it outputs "The number is positive."
- else if (number < 0) { ... }:
If the first condition is false, this checks if the number is less than zero. If true, it outputs "The number is negative."
- else { ... }:
If both previous conditions are false, this block executes, outputting "The number is zero."
7. return 0;:
This indicates that the program completed successfully.

Output: When the program runs, it prompts the user to enter a number and then checks if the number is positive, negative, or zero, displaying the appropriate message based on the condition.
```cpp
#include <iostream>
using namespace std;

int main() {
    int number;

    // Input: Get a number from the user
    cout << "Enter a number: ";
    cin >> number;

    // Conditional: Check if the number is positive, negative, or zero
    if (number > 0) {
        cout << "The number is positive." << endl;
    } else if (number < 0) {
        cout << "The number is negative." << endl;
    } else {
        cout << "The number is zero." << endl;
    }

    return 0;
}
```

### Loops:

####  Description of the Code:
1. #include <iostream>:
This line includes the input-output stream library, allowing the use of cout for output.
2. using namespace std;:
This allows the program to use standard functions and objects without the std:: prefix.
3. int main() { ... }:
This defines the main function, which is the starting point of the program.
4. For Loop:

- cout << "Using a for loop:" << endl;:
This prints a message indicating the start of the for loop section.
- for (int i = 1; i <= 5; i++) { ... }:
This loop starts with i at 1 and continues until i is 5. The i++ increments i by 1 after each iteration.
- cout << i << " ";:
Inside the loop, this prints the current value of i followed by a space.
5. While Loop:

- cout << "Using a while loop:" << endl;:
This prints a message indicating the start of the while loop section.
- int j = 1;:
This initializes the variable j to 1.
- while (j <= 5) { ... }:
This loop continues as long as j is 5 or less.
- cout << j << " ";:
Inside the loop, this prints the current value of j followed by a space.
- j++;:
This increments j by 1 after each iteration.
6. return 0;:
This indicates that the program completed successfully.

Output : Using a for loop:
1 2 3 4 5 
Using a while loop:
1 2 3 4 5 

```cpp
#include <iostream>
using namespace std;

int main() {
    // Using a for loop to print numbers 1 to 5
    cout << "Using a for loop:" << endl;
    for (int i = 1; i <= 5; i++) {
        cout << i << " ";
    }
    cout << endl;

    // Using a while loop to print numbers 1 to 5
    cout << "Using a while loop:" << endl;
    int j = 1;
    while (j <= 5) {
        cout << j << " ";
        j++;
    }
    cout << endl;

    return 0;
}

```

### Functions:

#### Description of the Code:
1. #include <iostream>:
This line includes the input-output stream library, allowing the use of cout for output.
2. using namespace std;:
This allows the program to use elements from the standard namespace without needing the std:: prefix.
3. Function Definitions:

- void greet() { ... }:
This function, named greet, has no parameters and returns no value (void). When called, it prints "Hello, User!".
- int add(int a, int b) { ... }:
This function, named add, takes two integer parameters (a and b) and returns their sum. It uses the return statement to send the result back to the caller.
4. int main() { ... }:
This defines the main function, which is where the program execution starts.
5. Calling Functions:

- greet();:
This line calls the greet function, which outputs "Hello, User!".
- int result = add(5, 3);:
This line calls the add function with the arguments 5 and 3. It stores the returned value (the sum) in the variable result.
6. Output:

- cout << "The sum is: " << result << endl;:
This prints the message "The sum is: " followed by the value of result, which is 8.
7. return 0;:
This indicates that the program completed successfully.

Outout : Hello, User!
The sum is: 8

```cpp
#include <iostream>
using namespace std;

// Function to greet the user
void greet() {
    cout << "Hello, User!" << endl;
}

// Function to add two numbers and return the result
int add(int a, int b) {
    return a + b;
}

int main() {
    // Call the greet function
    greet();

    // Call the add function and store the result
    int result = add(5, 3);
    cout << "The sum is: " << result << endl;

    return 0;
}
```

## All the basic concepts Implemented in Python

### Input/Output: 

#### Description of the Code:
1. print("Hello, World!"):
- This line uses the print function to output the string "Hello, World!" to the console.
- The text inside the quotes is displayed exactly as written.

Output : Hello, World!

```python
print("Hello, World!")
```

### Variables/Arrays:

#### Description of the Code:
1. Variable:

- age = 25:
This line declares a variable named age and assigns it the value 25, which represents the age of a person.
- print("Age:", age):
This line prints the text "Age:" followed by the value stored in the age variable.
2. List (Array):

- scores = [90, 85, 88, 92, 95]:
This line declares a list named scores that contains five integer values representing scores.
- print("Scores:", scores):
This line prints the text "Scores:" followed by the entire list of scores.
3. Loop:

- for score in scores::
This loop iterates over each value in the scores list.
- print(score, end=" "):
Inside the loop, this prints each score followed by a space instead of a new line.
- print():
This line prints a new line after all the scores have been printed.

Output : Age: 25   Scores: [90, 85, 88, 92, 95]
90 85 88 92 95 

```python
# Variable
age = 25  # This variable stores the age of a person
print("Age:", age)

# List (Array)
scores = [90, 85, 88, 92, 95]  # This list stores 5 scores
print("Scores:", scores)

# Loop through the list to print the scores
for score in scores:
    print(score, end=" ")  # Print each score in the list
print()  # New line after the scores
```

### Conditionals:

####  Description of the Code:
1. Input:

- number = int(input("Enter a number: ")):
This line prompts the user to enter a number. The input() function reads the input as a string, and int() converts it to an integer before storing it in the variable number.
2. Conditional Statements:

- if number > 0::
This checks if the number is greater than zero. If true, it executes the next line.
- print("The number is positive."):
This line prints "The number is positive." if the condition above is true.
- elif number < 0::
If the first condition is false, this checks if the number is less than zero. If true, it executes the next line.
- print("The number is negative."):
This line prints "The number is negative." if the condition above is true.
- else::
If both previous conditions are false (meaning the number is zero), this block executes.
- print("The number is zero."):
This line prints "The number is zero." if neither of the previous conditions is met.

Output : Enter a number: 5. 
   The number is positive.

   ```python
   # Input: Get a number from the user
number = int(input("Enter a number: "))

# Conditional: Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
   ```

### Loops:

#### Description of the Code:
1. For Loop:

- print("Using a for loop:"):
This prints a message indicating the start of the for loop section.
- for i in range(1, 6)::
This line initiates a for loop that iterates over a range of numbers from 1 to 5 (inclusive). The range(1, 6) function generates the numbers 1, 2, 3, 4, 5.
- print(i, end=" "):
Inside the loop, this prints the current value of i followed by a space instead of a newline.
- print():
This line prints a new line after all the numbers have been printed.
2. While Loop:

- print("Using a while loop:"):
This prints a message indicating the start of the while loop section.
- j = 1:
This initializes the variable j to 1.
- while j <= 5::
This initiates a while loop that continues as long as j is 5 or less.
- print(j, end=" "):
Inside the loop, this prints the current value of j followed by a space.
- j += 1:
This increments j by 1 after each iteration to eventually terminate the loop.
- print():
This line prints a new line after all the numbers have been printed.

Output : Using a for loop:
1 2 3 4 5 
Using a while loop:
1 2 3 4 5 
 
 ```python
 # Using a for loop to print numbers 1 to 5
print("Using a for loop:")
for i in range(1, 6):
    print(i, end=" ")  # Print each number in the range followed by a space
print()  # New line after the loop

# Using a while loop to print numbers 1 to 5
print("Using a while loop:")
j = 1
while j <= 5:
    print(j, end=" ")  # Print each number
    j += 1  # Increment j by 1
print()  # New line after the loop
 ```
### Functions:

#### Description of the code:
1. Function Definitions:

- def greet()::
This defines a function named greet. It doesn't take any parameters and is designed to greet the user.

- print("Hello, User!"):
This line is the body of the greet function. When the function is called, it prints "Hello, User!".

- def add(a, b)::
This defines a function named add that takes two parameters, a and b. The purpose of this function is to add these two numbers together.

- return a + b:
This line returns the sum of a and b to the caller of the function.
2. Main Part of the Program:

- greet():
This line calls the greet function, which outputs "Hello, User!" when executed.

- result = add(5, 3):
This line calls the add function with 5 and 3 as arguments. The result (which is 8) is stored in the variable result.
3. Output:

- print("The sum is:", result):
This line prints the message "The sum is:" followed by the value of result, which is 8.

Output : Hello, User!
The sum is: 8

```python
# Function to greet the user
def greet():
    print("Hello, User!")

# Function to add two numbers and return the result
def add(a, b):
    return a + b

# Main part of the program
greet()  # Call the greet function

# Call the add function and store the result
result = add(5, 3)
print("The sum is:", result)
```

## All the basic concepts Implemented in JavaScript:

### Input/Output: 

#### Description of the Code:
1. console.log("Hello, World!");:
- This line uses the console.log() function to output the string "Hello, World!" to the console.
- The text inside the quotes is displayed exactly as written.

Output : "Hello, World!

```javascript
console.log("Hello, World!");
```

### Variables/Arrays:

#### Description of the code:
1.Variable:

- let age = 25;:
This line declares a variable named age using the let keyword and assigns it the value 25, which represents the age of a person.
- console.log("Age:", age);:
This line prints the text "Age:" followed by the value stored in the age variable to the console.
2. Array:

- let scores = [90, 85, 88, 92, 95];:
This line declares an array named scores that contains five integer values representing scores.
- console.log("Scores:", scores);:
This line prints the text "Scores:" followed by the entire array of scores to the console.
3. Loop:

- console.log("Individual Scores:");:
This prints a message indicating that individual scores will be listed next.
- for (let i = 0; i < scores.length; i++) { ... }:
This line starts a for loop that iterates through the array scores. The loop runs from 0 to scores.length - 1, covering all indices of the array.
- console.log(scores[i]);:
Inside the loop, this prints the current score at index i.

Output : Age: 25
Scores: [90, 85, 88, 92, 95]
Individual Scores:
90
85
88
92
95

```javascript
// Variable
let age = 25;  // This variable stores the age of a person
console.log("Age:", age);

// Array
let scores = [90, 85, 88, 92, 95];  // This array stores 5 scores
console.log("Scores:", scores);

// Loop through the array to print the scores
console.log("Individual Scores:");
for (let i = 0; i < scores.length; i++) {
    console.log(scores[i]);  // Print each score in the array
}
```

### Conditionals:

#### Description of the code:
1. Input:

- let number = prompt("Enter a number:");:
This line prompts the user to enter a number. The prompt() function displays a dialog box that allows the user to input data. The entered value is stored as a string in the variable number.
2. Type Conversion:

- number = Number(number);:
This converts the input string to a number type using the Number() function, allowing for numerical comparisons in the following conditionals.
3. Conditional Statements:

- if (number > 0) { ... }:
This checks if the number is greater than zero. If true, the code inside the block executes.

- console.log("The number is positive.");:
This line prints "The number is positive." if the condition above is true.
- else if (number < 0) { ... }:
If the first condition is false, this checks if the number is less than zero. If true, the code inside this block executes.

- console.log("The number is negative.");:
This line prints "The number is negative." if the condition above is true.
- else { ... }:
If both previous conditions are false (meaning the number is zero), this block executes.

- console.log("The number is zero.");:
This line prints "The number is zero." if neither of the previous conditions is met.

Output : Enter a number: 5
The number is positive.

```javascript
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
```

### Loops: 

#### Description of the code:
1. For Loop:

- console.log("Using a for loop:");:
This line prints a message indicating the start of the for loop section.
- for (let i = 1; i <= 5; i++) { ... }:
This line initializes a for loop that starts with i equal to 1 and continues as long as i is less than or equal to 5. The i++ statement increments i by 1 after each iteration.
- console.log(i);:
Inside the loop, this line prints the current value of i.
2. While Loop:

- console.log("Using a while loop:");:
This line prints a message indicating the start of the while loop section.
- let j = 1;:
This initializes the variable j to 1.
- while (j <= 5) { ... }:
This line initiates a while loop that continues as long as j is less than or equal to 5.
- console.log(j);:
Inside the loop, this line prints the current value of j.
- j++;:
This increments j by 1 after each iteration to eventually terminate the loop.

Outout : Using a for loop:
1
2
3
4
5
Using a while loop:
1
2
3
4
5

```javascript
// Using a for loop to print numbers 1 to 5
console.log("Using a for loop:");
for (let i = 1; i <= 5; i++) {
    console.log(i);  // Print each number in the range
}

// Using a while loop to print numbers 1 to 5
console.log("Using a while loop:");
let j = 1;
while (j <= 5) {
    console.log(j);  // Print each number
    j++;  // Increment j by 1
}
```

### Functions:

#### Description of the code:
1. Function Definitions:

- function greet() { ... }:
Defines a function named greet that prints "Hello, User!" to the console when called.
- function add(a, b) { ... }:
Defines a function named add that takes two parameters, a and b, and returns their sum.
2. Function Calls:

- greet();:
Calls the greet function to display the greeting message.
- let result = add(5, 3);:
Calls the add function with the numbers 5 and 3, storing the returned value (which is 8) in the variable result.
- console.log("The sum is:", result);:
Displays the message "The sum is:" followed by the value of result.

Output : Hello, User!
The sum is: 8

```javascript
// Function to greet the user
function greet() {
    console.log("Hello, User!");
}

// Function to add two numbers
function add(a, b) {
    return a + b;  // Return the sum of a and b
}

// Call the greet function
greet();  // Output: Hello, User!

// Call the add function and display the result
let result = add(5, 3);  // result is 8
console.log("The sum is:", result);  // Output: The sum is: 8
```










