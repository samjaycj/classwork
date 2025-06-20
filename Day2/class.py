class NegativeNumberError(ValueError):
    pass
        

def get_positive_num():
    while True:
        try:
            num_str = input("Please enter positive number: ")
            num = float(num_str)

            if num<0 :
                raise NegativeNumberError("Number must be positive")
            return num
        except NegativeNumberError as e:
            print(e)
        except ValueError:
            print("Invalid Input")

if __name__ == "__main__":
    try:
        positive_num=get_positive_num()
        print(f"you have entered a Positive number: {positive_num}")
    except Exception as e:
        print(f"Exception: {e}")