import conversion

while (1):
    c = conversion.Conversion();
    print("--- NUMBER SYSTEMS CONVERSION ---")
    print("Convert from one base number system to another.\n[2] Binary\t[10] Decimal\n[8] Octal\t[16] Hexadecimal")
    print("[OTHER] Supports base 1 to base 36.")
    print("Note: Unary (base 1) uses only the digit 1.\n")

    while (1):
        c.getBaseInput()
        if (c.validBase(c.baseInput,False)):
            break
    while (1):
        c.getBaseOutput()
        if (c.validBase(c.baseOutput,True)): 
            break
    while (1):
        c.getNum()
        if (c.validInput()): 
            break
    print()
    c.printResult()
    
    print()
    while (1):
        ans = c.convertAgain()
        #if answer is valid, stop asking if user wants to convert
        if ans == '1' or ans == '0': 
            break

    print()
    if ans == '0': 
        print("Exiting...")
        break