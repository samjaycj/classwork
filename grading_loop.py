for student in range(1, 6):
    marks = 1
    while marks == 1:
        try:
            num = int(input(f"Enter Marks for student {student}: "))
            if num > 100 or num < 0:
                print("Entered marks is invalid. Marks should be in between 0 and 100")
                marks = 1
            elif num >= 75:
                print(f"Student{student} Grade is A")
                marks=0
            elif num >= 60:
                print(f"Student{student} Grade is B")
                marks=0
            elif num >= 50:
                print(f"Student{student} Grade is C")
                marks=0
            elif num >= 35:
                print(f"Student{student} Grade is S")
                marks=0
            else:
                print(f"Student{student} Grade is F")
                marks=0
        except ValueError:
            print("Invalid Input. Please enter valid Marks.")
            marks=1
