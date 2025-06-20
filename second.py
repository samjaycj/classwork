num_int = 10
num_float = float(num_int)
num_str = str(num_int)
str_num1 = "25"
str_num2 = "12.45"
int_num = int(str_num1)
float_num = float(str_num2)

print(f"Originally Integer: {num_int}, Type: {type(num_int)}")
print(f"Converted to float: {num_float}, Type: {type(num_float)}")
print(f"Converted to String: {num_str}, Type: {type(num_str)}")
print(f"Original number : {str_num1}, Type: {type(str_num1)}")
print(f"Converted to: {int_num}, Type: {type(int_num)}")
print(f"Original Number: {str_num2}, Type: {type(str_num2)}")
print(f"Converted to: {float_num}, Type: {type(float_num)}")
