print("\033c")

#Exercise odd or even number
number = int(input('Which number do you want to check?'))

# if number % 2:
#     print("It's a odd number")
# else:
#     print("It's a even number")
    
if number % 2 == 0:
    print("It's a even number.")
else:
    print("It's a odd number.")  