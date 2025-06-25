import csv

products= [
    {"id": "P001", "name": "Laptop", "price": 1200, "stock": 50},
    {"id": "P002", "name": "Mouse", "price": 25, "stock": 150},
    {"id": "P003", "name": "Keyboard", "price": 75, "stock": 70},
    {"id": "P004", "name": "Monitor", "price": 300, "stock": 25},
    {"id": "P005", "name": "Webcam", "price": 50, "stock": 15},
]

csv_file='products.csv'

field_names = ["id", "name", "price", "stock"]

try:
    with open(csv_file, mode='w', newline='') as csv_file:
        writer=csv.DictWriter(csv_file,fieldnames=field_names)
        writer.writeheader()
        writer.writerows(products)
        print(f"Successfuly Written {len(products)} rows to the CSV file.")
except IOError as e:
    print(f"Error in writing file {e}")
except Exception as e:
    print(e)