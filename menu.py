# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

menu_dashes = "-" * 38

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

order_list = []

# Launch the store and present a greeting to the customer

print(menu_dashes)
print("Welcome to Chez Sam's Tasty Truck.")
print(menu_dashes)

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order from? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    print()
    menu_category = input("Type menu number: ")
    print()
    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"Please select from the {menu_category_name} below:")
            print()
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            print()
            menu_selection = input(f"What item # would you like to order?" ) 

    
            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                
               
                   

                # Convert the menu selection to an integer
                
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                
                if menu_selection in menu_items.keys():
                    item_selection = menu_items[menu_selection]
                    item_name = item_selection["Item name"]
                    item_price = item_selection["Price"]
                
                    # Store the item name as a variable
                
                    item_selection = menu_items[menu_selection]
                    print(f"You have selected {item_selection}")

        

                
                    # Ask the customer for the quantity of the menu item
                    item_quantity = input(f"How many would you like to order?")

                    # Check if the quantity is a number, default to 1 if not
                    if item_quantity.isdigit():
                        item_quantity = int(item_quantity)
                                 

                    else:
                        item_quantity = 1
        
                    
    
                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                         "Item name": item_name,
                         "Price": item_price,
                         "Quantity": item_quantity
                    })
                
  
                    # Tell the customer that their input isn't valid
                else: print(f"Please make a valid selection.")
            else:
                print(f"You did not select a menu option.")    # Tell the customer they didn't select a menu option
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        print()
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
       
            
        # 5. Check the customer's input

                # Keep ordering
        match keep_ordering.lower():


            case 'y':
                place_order = True
                                 
            # Exit the keep ordering question loop
                break
                # Complete the order
            case 'n':
                place_order = False              
                    
                # Since the customer decided to stop ordering, thank them for
                # their order
                print(f"Thank you for your order.")
                # Exit the keep ordering question loop

                break
                # Tell the customer to try again
            case _:
                print(f"Please select a valid option")

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order_list)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for item in range(len(order_list)):

    # 7. Store the dictionary items as variables
    item_name = order_list[item]["Item name"]  
    item_price = order_list[item]["Price"] 
    item_quantity = order_list[item]["Quantity"] 

    # 8. Calculate the number of spaces for formatted printing
    item_name_length = len(item_name)
    item_price_length = len(str(item_price))
    #item_quantity_length = len(str(item_quantity))

    spaces_for_name = 26 - item_name_length
    spaces_for_price = 9 - item_price_length
    #spaces_for_quantity = 10 - item_quantity_length
    
    
    # 9. Create space strings
    space_name = ' ' * spaces_for_name
    space_price = ' ' * spaces_for_price
    #space_quantity = ' ' * spaces_for_quantity
   
    # 10. Print the item name, price, and quantity
    print(f"{item_name}{space_name}| ${item_price}{space_price}| {item_quantity}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.

total_order_cost = sum(item["Price"] * item["Quantity"] for item in order_list)

print(f"\nTotal Cost: ${total_order_cost:.2f}")

