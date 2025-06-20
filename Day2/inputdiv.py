try:
    num_numerator = input("Enter the Numerator: ")
    numerator = float(num_numerator)
    num_denominator = input("Enter the Denominator: ")
    denominator = float(num_denominator)

    results = numerator/denominator

    print(f"You entered: Numerator {numerator} & Denominator {denominator}")
    print(f"The result is: {results}")

except ValueError:
    print("Invalid Inputs detected. Enter valid numbers for the Numerator and Denominator")

except ZeroDivisionError:
    print("Cannot devide by Zero")

except Exception as e:
    print(f"An Error Occured: {e}")