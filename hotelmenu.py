#Define the menu of restarant
menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':80,
    'Salad':70,
    'Coffee':80,
}

#Greet
print("Welcome to our Restraurant!")
print("Pizza: 40\nPasta: 50\nBurger: 80\nSalad: 70\nCoffee: 80")
print(menu)
order_total=0

item_1 = input('Enter the name of item you want to order = ')

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"{item_1} not avaiable")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 =input("Enter the name of second item = ")
    if item_2 in  menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"{item_2} not avaiable")

print(f"The total numbers of to be pay {order_total}")