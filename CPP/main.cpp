#include <iostream>
#include "conversion.h"
using namespace std;

int main() {
    int ans = 1;
    while (ans) {
        Conversion* c = new Conversion();
        cout << "--- NUMBER SYSTEMS CONVERSION ---" << endl;
        cout << "Recommended: 10 (Decimal), 2 (Binary), 8 (Octal), 16 (Hexadecimal)." << endl;
        cout << "Supports base 2 up to base 36." << endl << endl;
        
        do {
            c->getBaseInput();
        } while (!c->validBase(c->baseInput));
        do {
            c->getBaseOutput();
        } while (!c->validBase(c->baseOutput));
        do {
            c->getInput();
        } while (!c->validInput(c->input));
        cout << endl;
        c->printResult();
        cout << endl << endl;

        cout << "Convert another?" << endl;
        cout << "[1] Yes" << endl << "[0] No" << endl;
        cout << "Choice: ";
        cin >> ans;

        cout << endl;
        if (!ans) cout << "Exiting...";
    }
    return 0;
}