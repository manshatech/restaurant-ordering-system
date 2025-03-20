menu= {
    'Sandwich':100,
    'Pasta':120,
    'Burger':70,
    'Fries':110,
    'Cold Coffee':150,
    'Noodles':120,
    'Brownie':170
}

print('Welcome to Python Restaurant!!\nHere is our Menu.')
print('Sandwich : Rs100\nPasta : Rs120\nBurger : Rs70\nFries : Rs110\nCold Coffee : Rs150\nNoodles : Rs120\nBrownie : Rs170')

order_total=0
item_1=input('What would you like to have?')
if item_1 in menu:
    order_total+=menu[item_1]
    print('Your item has been added to your order!!')
else:
    print('Sorry!!Your ordered item is not available yet.')

num_items=5
for i in range(num_items):
    another_order = input('Do you want to add anything else? (Yes/No) ')
    if another_order.lower() == 'yes':
        item_2 = input('Enter the item you want to add: ')
        if item_2 in menu:
            order_total += menu[item_2]
            print('Your item has been added to your order!!')
        else:
            print('Sorry! The item you ordered is not available yet.')
    else:
        print('Thank you for your order!')
        break  # If the user says "No", we stop asking for more items

# Displaying the total amount
print(f'The total amount of items to pay is Rs{order_total}')
