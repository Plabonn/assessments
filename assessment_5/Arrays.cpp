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
