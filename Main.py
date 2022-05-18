def ConvertToRoman(code):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    Rom = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    Result = ""
    while code:
        Divi = code // num[i]
        code %= num[i]
        while Divi:
            print("("+Rom[i], end=")")
            Result = Result + Rom[i]
            Divi -= 1
        i -= 1
    return Result


if __name__ == "__main__":

    input("Welcome to the converter from arabig or decimal numbers to Roman numbers")
    number = str(input("Write a number"))
    if not number:
         print("it is empty")
    elif number.replace(".","").isnumeric():
        number = round(float(number))
        if number > 0:
            if number < 1000:
                ConvertToRoman(number)
            else:
                print("the number must be between 1 and 1000")
        else:
            print("only positive numbers or decimal with . are allowed")

    else:
        print("only positive numbers or decimal with . are allowed")