print("\033c")

print('Welcome to Python Pizza Deliveries!')
size = input('What size Pizza do you want? S , M or L \n')
add_pepperoni = input('Do you want pepperoni? Y or N \n')
extra_cheese = input('Do you want extra cheese ? Y or N \n')
price =0
pizza =0

if size == 'S':
    price=15
    
    pizza = 2
    total1 = price + pizza
    
    if add_pepperoni == 'Y':
        print(f'Your final bill is $ {total1}')
    elif add_pepperoni == 'N':
        print(f'price is $ {price}') 

elif size == 'M':
    price=20
    
    pizza = 3
    total = price + pizza
    
    if add_pepperoni == 'Y':
        print(f'Your final bill is $ {total}')
    elif add_pepperoni == 'N':
        print(f'price is $ {price}') 

elif size == 'L':
    price=25
    
    pizza = 3
    total = price + pizza
    
    if add_pepperoni == 'Y':
         print(f'Your final bill is $ {total}')
    elif add_pepperoni == 'N':
        print(f'price is $ {price}') 
    
else:
    print("None")
    
    
    
    

   