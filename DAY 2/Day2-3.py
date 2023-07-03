print("\033c")

#DAY2-3 Challenge(Tip calculator)
age = input("What is your current age.\n")
main_age = 90
cal = int(main_age) - int(age) 
# print((cal))
x = cal * 365 
# print(x)
y = cal * 52 
# print(y)
z = cal * 12 
# print(z)

print(f'You have {x} days , {y} weeks and {z} months')