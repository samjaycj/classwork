import csv
csv_file = 'employee.csv'

target_dep = 'IT'

print (f"Attempting to read employee data from file {csv_file}")

filtered_emp = []

try:
    with open(csv_file, mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            if row.get('Department') == target_dep:
                filtered_emp.append(row)
    print(f"...... Employees in {target_dep} Department ......")
    if filtered_emp:
        for emp in filtered_emp:
            print(emp['Name'])
            
except FileNotFoundError as e:
    print(f"File error: {e}")
except Exception as e:
    print(f"Error Occured: {e}")