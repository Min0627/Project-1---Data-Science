#!/usr/bin/env python
# coding: utf-8

# In[7]:


# inventory dictionary
inventory = {}

while True:
    # prompt user for an action
    prompt = input("\nChoose an option: 1. Add | 2. Update | 3. View | 4. Stop |\nYour Option: ").strip().lower()

    if prompt == "add" or prompt == "1":
        product = input("Enter product name: ").strip().capitalize()
        price = float(input("Enter price (RM): "))
        quantity = int(input("Enter quantity: "))
        inventory[product] = [price, quantity]
        print(f"{product} added successfully!")

    elif prompt == "update" or prompt == "2":
        product = input("Enter product name to update: ").strip().capitalize()
        if product in inventory:
            price = float(input("Enter new price (RM): "))
            quantity = int(input("Enter new quantity: "))
            inventory[product] = [price, quantity]
            print(f"{product} updated successfully!")
        else:
            print("Product not found!")

    elif prompt == "view" or prompt == "3":
        if inventory:
            print("\nCurrent Inventory:")
            for product, details in inventory.items():
                print(f"{product}: RM{details[0]}, Quantity: {details[1]}")
        else:
            print("Inventory is empty.")

    elif prompt == "stop" or prompt == "4":
        print("\nExiting program. Have a great day!")
        break

    else:
        print("Invalid option. Please try again.")


# In[ ]:




