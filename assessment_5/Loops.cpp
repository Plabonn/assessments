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
