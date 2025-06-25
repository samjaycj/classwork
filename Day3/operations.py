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

def update_stocks(prod_id, quantity):
    found = False
    qty=float(quantity)
    for product in inventory:
        if prod_id == product['id']:
            if qty + product['stock'] >=0 :
                product['stock'] += qty
                print(f"Updated stocks for {product['name']}: {product['stock']}")
            else:
                print(f"Error: Not enough stocks available for {product['name']}")
            found = True
            break
    if not found:
        print(f"Error: Product id {prod_id} not found")

# update_stocks(input('Enter Product Id: '), input('Enter Quantity: '))

def get_low_stocks(threshold):
    threshold=int(threshold)
    lowstocks = []
    for product in inventory:
        if product['stock'] < threshold:
            lowstocks.append(product['name'])
    print(f"Low stock products are {lowstocks}")        

get_low_stocks(30)
