import conversion

while (1):
    c = conversion.Conversion();
    print("--- NUMBER SYSTEMS CONVERSION ---")
    print("Recommended: 10 (Decimal), 2 (Binary), 8 (Octal), 16 (Hexadecimal).")
    print("Supports base 2 up to base 36.\n")

    while (1):
        c.getBaseInput()
        if (c.validBase(c.baseInput)): break
    while (1):
        c.getBaseOutput()
        if (c.validBase(c.baseOutput)): break
    while (1):
        c.getNum()
        if (c.validInput()): break
    print()
    c.printResult()
    
    print()
    while (1):
        print("Convert another?")
        print("[1] Yes\n[0] No\nChoice:",end=' ')
        ans = int(input())
        if ans == 1 or ans == 0:
            break

    print()
    if not ans: 
        print("Exiting...")
        break