class Conversion:
    baseInput = None
    baseOutput = None
    num = None

    #empty constructor
    def __init__(self): 
        return

    #checks validity of base
    #base must always be a number, base of output must not be the same as base of input
    #up to 36 (10 digits + 26 letters)
    def validBase(self,base,isOutput): 
        if ' ' in base: #spaces within the string are invalid
            return False
        if (isOutput):
            return base != self.baseInput and base.isnumeric() and (int(base) > 0) and (int(base) < 37)
        else:
            return base.isnumeric() and (int(base) > 0) and (int(base) < 37)

    def validInput(self):
        if (int(self.baseInput) > 10):
            for i in self.num:
                #no case for digits because they will always be valid for bases above 10
                if i.isalpha() and (ord(i) - 55 >= int(self.baseInput)): #ord returns ascii code
                    return False
        else:
            #base 10 and lower only make use of digits, so any letters are invalid
            if not self.num.isnumeric():
                return False
            for i in self.num:
                if self.baseInput == '1' and (int(i) != 1): #unary only uses the digit 1
                    return False
                if self.baseInput != '1' and (int(i) >= int(self.baseInput)):
                    return False
        return True

    def getBaseInput(self):
        self.baseInput = input("Enter base of input: ").strip() #removes whitespaces only at the beginning and end

    def getBaseOutput(self):
        self.baseOutput = input("Enter base to convert to: ").strip()

    def getNum(self):
        self.num = input("Enter number to convert: ").replace(" ","") #removes all whitespaces within num

    #returns string instead of int to support bases >10
    def convertNum(self):
        self.baseInput = int(self.baseInput)
        self.baseOutput = int(self.baseOutput)

        if (self.baseInput == 1):
            n = len(self.num) #length of string ie how many 1s inputted
        else: 
            n = int(self.num,self.baseInput)

        ans = "" #initializing string to hold result

        if (self.baseOutput == 1):
            for i in range(n):
                ans += '1'
                #group digits into 5s, exclude whitespaces
                if (sum(len(i) for i in ans.split()) % 5 == 0):
                    ans += ' '
            return ans

        while (n != 0):
            rem = n % self.baseOutput 
            if (rem < 10):
                ch = chr(rem + 48) #0-9
            else:
                ch = chr(rem + 55) #A-Z, capital
            ans += ch

            #group decimal digits into 3s, others into 4s
            if (self.baseOutput == 10 and sum(len(i) for i in ans.split()) % 3 == 0):
                ans += ' '
            elif (self.baseOutput != 10 and sum(len(i) for i in ans.split()) % 4 == 0):
                ans += ' '

            #cast to int because it auto converts to long (?) basta madaghan leading zeroes sa resulta lol
            n = int(n / self.baseOutput) #this line is why base 1 is a special case

        #flips string as the result from above is reverse of the final answer
        return ans[::-1].lstrip() #removes leading whitespaces

    def printResult(self):
        print("--- RESULT ---")
        print("(Base ",self.baseInput,") ",self.num," -> (Base ",self.baseOutput,") ",self.convertNum(), sep="")

    def convertAgain(self):
        print("Convert another?")
        print("[1] Yes\t[0] No")
        return input("Choice: ")