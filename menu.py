menu_items = [
  {
    "Item name": "Tonkotsu ramen",
    "Price": float(9.99),
    "Quantity": int(1)
  },
  {
    "Item name": "Hunan Chicken",
    "Price": float(8.99),
    "Quantity": int(1)
  },
  {
    "Item name": "Pork Buns",
    "Price": float(5.99),
    "Quantity": int(1)
  },
  {
    "Item name": "Spicy Tuna Roll",
    "Price": float(7.99),
    "Quantity": int(1)
  }
]

print("Welcome to Chef Sam's Food Truck!")

print("Here is our menu:")
for item in menu_items:
    print(f"{item['Item name']} - ${item['Price']}")

while True:
    menu_selection = input("Which item would you like to order? (Enter the item name or 'done' to finish): ")
    
    if menu_selection.lower() == 'done':
        break
    
    found = False
    for item in menu_items:
        if menu_selection.lower() == item['Item name'].lower():
            quantity = int(input(f"How many {item['Item name']} would you like to order? "))
            item['Quantity'] += quantity
            found = True
            break
    
    if not found:
        print("Item not found in the menu. Please try again.")

