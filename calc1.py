str_in1 = input("Enter the input number 1: ")
str_in2 = input("Enter the input number 2: ")

try:
    conv_num1 = int(str_in1)
    conv_num2 = int(str_in2)
    tot = conv_num1 + conv_num2
except ValueError:
    try:
        conv_num1 = float(str_in1)
        conv_num2 = float(str_in2)
        tot = conv_num1 + conv_num2
    except ValueError:
        tot = "Invalid input value detected. Enter valid numbers for input 1 and input 2"

print(tot)
