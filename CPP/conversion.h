#include <iostream>
#include <string>
using namespace std;

class Conversion {
    public:
    int baseInput, baseOutput;
    string input;

    //checks if user inputted base is valid
    //2 - binary, 36 - (10 digits + 26 letters)
    bool validBase(int base) {
        return base > 1 && base < 37;
    }

    //checks if user-inputted number is valid given the chosen base
    bool validInput(string input) {
        if (baseInput > 10) {
            for (int i = 0; i < input.size(); i++) {
                //cout << input[i] - '0' << endl;
                if ((input[i] - '0') - 7 >= baseInput) {
                    //cout << i << " " << input[i] - '0' << endl;
                    return false;
                }
            }
        } else {            
            for (int i = 0; i < input.size(); i++) {
                if (input[i] - '0' >= baseInput) { //convert input[i] to int
                    return false;
                }
            }
        }
        return true;
    }

    void getBaseInput() {
        cout << "Enter base of input: ";
        cin >> baseInput;
    }

    void getBaseOutput() {        
        cout << "Enter base to convert to: ";
        cin >> baseOutput;
    }    

    void getInput() {        
        cout << "Enter number to convert: ";
        cin >> input;
    }

    //method to do the conversion
    //string return type to support bases 11-36
    string convertNum() {
        unsigned long long inputNum = stol(input, 0, baseInput);

        //stoi always returns a decimal number, so the resulting value can be returned directly
        if (baseOutput == 10) {
            return to_string(inputNum); //convert to string from int
        }

        unsigned long long n = inputNum;
        string ans;

        while (n != 0) {
            unsigned long long rem = 0;
            char ch;

            rem = n % baseOutput;
            if (rem < 10) {
                ch = rem + 48; //0-9
            } else {
                ch = rem + 55; //letters
            }

            ans += ch;
            n /= baseOutput;
        }

        //flip string because the result of the conversion above is reversed
        int i = 0, j = ans.size() - 1;
        while (i <= j) {
            swap(ans[i], ans[j]);
            i++;
            j--;
        }

        return ans;
    }

    void printResult() {
        cout << "--- RESULT ---" << endl;
        cout << "(Base " << baseInput << ") " << input << " -> (Base " << baseOutput << ") " << convertNum();
    }
};