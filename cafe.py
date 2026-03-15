menu = {
    "Pizza": 60,
    "Burger": 50,
    "Pasta": 40,
    "Coffee": 80,
    "Tea": 30
}

print("Welcome to our Tejas Cafe...!")
print("***********************************************************")
print("Pizza:60\nBurger:50\nPasta:40\nCoffee:80\nTea:30")
print("***********************************************************")
order_total = 0

item_1 = input("Enter the name of the item you want to order: ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available in our menu!")

another_order = input("Do you want to order another item? (yes/no): ")

if another_order == "yes":
    item_2 = input("Enter the name of the second item: ")

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available in our menu!")

print(f"Your Total Order Amount is: {order_total}")         
print("***********************************************************")