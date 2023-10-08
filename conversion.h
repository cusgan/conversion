#include <iostream>
#include <string>
using namespace std;

class Conversion {
    public:
    int baseInput, baseOutput, inputNum;
    string input;

    bool validInput(int base) {
        return base == 10 || base == 2 || base == 8 || base == 16;
    }
    
    void getInput() {        
        cout << endl << "Enter number to convert: ";
        cin >> input;
        switch (baseInput) {
            case 10:
                inputNum = stoi(input);
                break;
            case 2:
                inputNum = stoi(input, 0, 2);
                break;
            case 8:
                inputNum = stoi(input, 0, 8);
                break;
            case 16:    
                inputNum = stoi(input, 0, 16);
                break;
        }
    }

    void getBaseInput() {
        cout << endl << "Enter base of input: " << endl;
        cout << "- 10 (Decimal)" << endl << "- 2 (Binary)" << endl << "- 8 (Octal)" << endl << "- 16 (Hexadecimal)" << endl;
        cout << "Base: ";
        cin >> baseInput;
    }

    void getBaseOutput() {        
        cout << endl << "Enter base to convert to: " << endl;
        cout << "- 10 (Decimal)" << endl << "- 2 (Binary)" << endl << "- 8 (Octal)" << endl << "- 16 (Hexadecimal)" << endl;
        cout << "Base: ";
        cin >> baseOutput;
    }

    int toDecimal() {
        return inputNum;
    }

    int toBinary() {
        int bin = 0, i = 1, n = inputNum, rem;

        while (n != 0) {
            rem = n % 2;
            n /= 2;
            bin += rem * i;
            i *= 10;
        }

        return bin;
    }

    int toOctal() {
        int oct = 0, i = 1, n = inputNum, rem;

        while (n != 0) {
            rem = n % 8;
            n /= 8;
            oct += rem * i;
            i *= 10;
        }

        return oct;
    }

    string toHexadecimal() {
        int n = inputNum;
        string ans;

        while (n != 0) {
            int rem = 0;
            char ch;

            rem = n % 16;
            if (rem < 10) {
                ch = rem + 48;
            } else {
                ch = rem + 55;
            }

            ans += ch;
            n /= 16;
        }

        int i = 0, j = ans.size() - 1;
        while (i <= j) {
            swap (ans[i], ans[j]);
            i++;
            j--;
        }

        return ans;
    }

    void printResult() {
        cout << endl << "--- RESULT ---" << endl;
        cout << "(Base " << baseInput << ") " << input << " -> (Base " << baseOutput << ") ";
        switch (baseOutput) {
            case 10:
                cout << toDecimal();
                break;
            case 2:
                cout << toBinary();
                break;
            case 8:
                cout << toOctal();
                break;
            case 16:
                cout << toHexadecimal();
                break;
        }
    }
};