print("\033c")

#nested if statements and elif statements
# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm?"))

# if height >= 120:
#     print('can ride the rollercoaster')
    
#     age = int(input("What is your age?"))
    
#     if age <= 18:
#         print('Pay $7')
#     else:
#         print("Pay $12")
    
    
# else:
#     print("Can't ride the rollercoaster,first grow much taller")
    
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?"))

if height >= 120:
    print('can ride the rollercoaster')
    
    age = int(input("What is your age?"))
    price = 0
    
    if age < 12:
        price=5
        print(f'price is $ {price}')
        
    elif age <= 18:
        price=7
        print(f'price is $ {price}')  
    else:
        price=12
        print(f'price is $ {price}')
        
    photo = input("Do you want a photo?")
    freak = 3
    total = price + freak
    
    if photo == 'yes':
        print(f'your account is $ {total}')
    elif photo == 'no':
        print(f'price is $ {price}') 
    
else:
    print("Can't ride the rollercoaster,first grow much taller")