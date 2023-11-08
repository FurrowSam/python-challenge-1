menu_items = [    
  {
    "Item name": 'Tonkotsu ramen',
    "Price": float(19.99),
    "Quantity": int(1)
  },
  {
    "Item name": 'Hunan Chicken',
    "Price": float(17.99),
    "Quantity": int(1)
  },
  {
    "Item name": 'Pork Buns',
    "Price": float(9.99),
    "Quantity": int(3)
  },
  {
    "Item name": 'Spicy Tuna Roll',
    "Price": float(12.99),
    "Quantity": int(1)
  },
  {
    "Item name": 'Blistered Shishito Peppers',
    "Price": float(12.99),
      "Quantity": int(1)
  }
]

menu_dashes = "-" * 33

print(menu_dashes)
print("Welcome to Chef Sam's Food Truck!")
print(menu_dashes)



while True:
    
    print(menu_dashes)
    print("Please select from our menu below")
    print(menu_dashes)

    i = 1
    menu_selection = { }


    for item in menu_items:
        for value in item.items():
         print(f"{value}")
        


        menu_selection[i] = value
        i += 1
    
    # menu_selection = input("Please select your items or Q to Quit.")



    # if menu_selection == 'Q':
    #     break
    # elif menu_selection.isdigit():
    #     if int(menu_selection) in menu_items.keys():
            
    #         menu_selection = menu_items[int(menu_selection)]

    #         print(menu_dashes)
    #         print(f"You have selected {menu_selection}")


  
             