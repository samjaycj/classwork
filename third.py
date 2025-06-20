favourite_no = input("Please enter number:")
try:
    converted_num = int(favourite_no)
    print(f"\nSuccessfully converted input to integer: {converted_num}")
    total = converted_num + 10
    print(f"Added 10 to the input number, {converted_num}. Total is {total}. Type: {type(total)}")

except ValueError:
    try:
        converted_num = float(favourite_no)
        print(f"\nSuccessfully converted input to integer: {converted_num}")
        total = converted_num + 10
        print(f"Added 10 to the input number, {converted_num}. Total is {total}. Type: {type(total)}")

    except ValueError:
        print(f"\nInvalid input: {favourite_no} cannot be converted to a number")
        print("Enter a valid number")
