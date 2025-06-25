import csv

inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200, "stock": 50},
    {"id": "P002", "name": "Mouse", "price": 25, "stock": 150},
    {"id": "P003", "name": "Keyboard", "price": 75, "stock": 70},
    {"id": "P004", "name": "Monitor", "price": 300, "stock": 25},
    {"id": "P005", "name": "Webcam", "price": 50, "stock": 15},
]

print("..... Initial Inventory .....")
for product in inventory:
    print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Stock: {product['stock']}")
print("\n")

def get_low_stocks(threshold):
    file_name='low_stocks.csv'
    fields = ['Name']
    threshold=int(threshold)
    lowstocks = []
    for product in inventory:
        if product['stock'] < threshold:
            lowstocks.append({'Name':product['name']})
    print(f"Low stock products are {lowstocks}") 

    
    try: 
        with open(file_name, mode='w', newline='') as file_name:
            writers = csv.DictWriter(file_name, fieldnames=fields)
            writers.writeheader()
            writers.writerows(lowstocks)
    except IOError as e:
        print(f"Error writing file: {e}")
    except Exception as e:
        print(e)


get_low_stocks(30)