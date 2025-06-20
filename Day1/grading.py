try:
    num = int(input("Enter Marks: "))
    if num > 100 or num < 0:
        print("Entered marks is invalid. Marks should be in between 0 and 100")
    elif num >= 75:
        print("Your Grade is A")
    elif num >= 60:
        print("Your Grade is B")
    elif num >= 50:
        print("Your Grade is C")
    elif num >= 35:
        print("Your Grade is S")
    else:
        print("Your Grade is F")
except ValueError:
    print("Invalid Input. Please enter a valid Marks.")
