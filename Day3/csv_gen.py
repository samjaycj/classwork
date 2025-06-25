import pandas as pd

# Create the employee data
data = {
    "EmployeeID": [1, 2, 3, 4, 5],
    "Name": ["Alice Smith", "Bob Johnson", "Carol White", "Dan Brown", "Eve Black"],
    "Department": ["HR", "IT", "Finance", "Marketing", "IT"],
    "Salary": [55000, 67000, 72000, 60000, 68000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to a CSV file
df.to_csv("employee.csv", index=False)