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
