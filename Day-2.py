print("\033c")

# print("Charmaine"[8])

#DAY2-1 Challenge(Input calculator)
# name = input("Enter a two digit number?\n")
# first = print(name[0])
# second = print(name[1])

# third = int(name[0]) + int(name[1])
# print(third)
      
# print(3 * 3 + 3 / 3 - 3)

#DAY2-2 Challenge(BMI calculator)
# height = input('enter your height in m:\n')
# weight = input('enter your weight in m:\n')

# third =   int(weight) / float(height) **2
# print(round(third))

#DAY2-3 Challenge(Tip calculator)
# age = input("What is your current age.\n")
# main_age = 90
# cal = int(main_age) - int(age) 
# print((cal))
# x = cal * 365 
# print(x)
# y = cal * 52 
# print(y)
# z = cal * 12 
# print(z)

# print(f'You have {x} days , {y} weeks and {z} months')

#DAYfinal-exam Challenge(Tip calculator)
print('Welcome to the tip calculator.')
first = input('What was the total bill?')
second = input('What percentage tip would you like to give? 10 12 or 15?.')
third = input('How many people to spilt the bill?')

percentage = int(second)/100 * float(first)
semi_percentage = float(first) + float(percentage)
final_percentage = float(semi_percentage) / int(third)
forth = (round(final_percentage,2))
print(f'Each person should pay: {forth}')

