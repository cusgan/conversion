class Conversion:
    baseInput = None
    baseOutput = None
    num = None

    #empty constructor
    def __init__(self): 
        return

    #checks validity of base
    #2 - binary, 36 - (10 digits + 26 letters)
    def validBase(self,base): 
        return (base > 1) and (base < 37)

    def validInput(self):
        if (self.baseInput > 10):
            for i in self.num:
                #no case for digits because they will always be valid for bases above 10
                if i.isalpha() and (ord(i) - 55 >= self.baseInput): #ord returns ascii code
                    return False
        else:
            #base 10 and lower only make use of digits, so any letters are invalid
            if not self.num.isnumeric():
                return False
            for i in self.num:
                if (int(i) >= self.baseInput):
                    return False
        return True

    def getBaseInput(self):
        print("Enter base of input:",end=' ')
        self.baseInput = int(input())

    def getBaseOutput(self):
        print("Enter base to convert to:",end=' ')
        self.baseOutput = int(input())

    def getNum(self):
        print("Enter number to convert:",end=' ')
        self.num = input()

    #returns string instead of int to support bases >10
    def convertNum(self):
        n = int(self.num,self.baseInput)

        #int() returns a decimal number, so if the output is to be dec, the resulting value can be returned directly
        if (self.baseOutput == 10):
            return str(n)

        ans = ""
        while (n != 0):
            rem = n % self.baseOutput
            if (rem < 10):
                ch = chr(rem + 48) #0-9
            else:
                ch = chr(rem + 55) #A-Z, capital

            ans += ch
            #cast to int because it auto converts to long (?) basta madaghan leading zeroes sa resulta lol
            n = int(n / self.baseOutput)

        #flips string as the result from above is reverse of the final answer
        return ans[::-1] 

    def printResult(self):
        print("--- RESULT ---")
        print("(Base ",str(self.baseInput),") ",self.num," -> (Base ",str(self.baseOutput),") ",self.convertNum(), sep="")