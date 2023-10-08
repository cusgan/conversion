#include <iostream>
#include "conversion.h"
using namespace std;

int main() {
    int ans = 1;
    while (ans) {
        Conversion* c = new Conversion();
        cout << "--- NUMBER SYSTEMS CONVERSION ---" << endl;
        
        do {
            c->getBaseInput();
        } while (!c->validInput(c->baseInput));
        do {
            c->getBaseOutput();
        } while (!c->validInput(c->baseOutput));
        c->getInput();
        c->printResult();

        cout << endl << endl << "Convert another?" << endl;
        cout << "[1] Yes" << endl << "[0] No" << endl;
        cout << "Choice: ";
        cin >> ans;

        cout << endl;
        if (!ans) cout << "Exiting...";
    }
    return 0;
}