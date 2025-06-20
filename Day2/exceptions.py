try:
    userin = input("Enter list of numbers: ")
    numstr = userin.split(',')
    nums = []

    if not numstr or (len(numstr)==1 and not numstr[0]):
        raise IndexError('The list is empty.')
    
    for num in numstr:
        nums.append(int(num.strip()))

except ValueError:
    print ("Error: Invalid Input. Numbers only")
except IndexError as e:
    print(f"Error: {e}")
else:
    tot = sum(nums)
    print (f"Total of the entered numbers is {tot}")
finally:
    print("Completed Operation")
    