import json
from datetime import datetime

products= {"inventory" : [
    {"id": "P001", "name": "Laptop", "price": 1200, "stock": 50},
    {"id": "P002", "name": "Mouse", "price": 25, "stock": 150},
    {"id": "P003", "name": "Keyboard", "price": 75, "stock": 70},
    {"id": "P004", "name": "Monitor", "price": 300, "stock": 25},
    {"id": "P005", "name": "Webcam", "price": 50, "stock": 15},
], "last_updated": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}

json_file='products.json'

print(f"Attempting to write product data to {json_file}...")

try:
    with open(json_file, mode='w', encoding='utf-8') as json_file:
        json.dump(products, json_file, indent=4)
        print(f"Successfully wrote product data to {json_file}")

except IOError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Undefined Error: {e}")