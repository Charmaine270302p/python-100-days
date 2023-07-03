print("\033c")

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