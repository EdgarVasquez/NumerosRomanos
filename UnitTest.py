def Validation(Number):
    Number = str(Number)
    Answer = ""
    if not Number:
        Answer = "Is empty"
    elif Number.replace(".", "").isnumeric():
        if int(Number) > 0:
            if int(Number) < 1000:

                Answer = "Correct"
            else:
                Answer = "the number must be between 1 and 1000"
        else:
            Answer = "only positive numbers or decimal with . are allowed"
    else:
        Answer = "only positive numbers or decimal with . are allowed"

    return Answer