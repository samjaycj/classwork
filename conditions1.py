try:
    num = int(input("Enter Number: "))

    if num > 0:
        print(f"The number {num} is positive")
    elif num < 0:
        print(f"The number {num} is negative")
    else:
        print("The number is zero")
except ValueError:
    print("Invalid Input. Please enter a valid whole numeber.")
