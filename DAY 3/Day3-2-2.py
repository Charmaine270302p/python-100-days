print("\033c")

#DAY3-2 Challenge(BMI calculator)
height = float(input('enter your height in m:'))
weight = float(input('enter your weight in m:'))

third =   (weight) / (height) **2

if third < 18.5:
    print(f'Under {third} they are underweight')

elif third >= 18.5 and third <= 25:
   print(f'Over 18.5 below 25 they have a normal weight')
 
elif third >= 25 and third <= 30:
    print(f'Over 25 below 30 they have a overweight')
    
elif third >= 30 and third <= 35:
    print(f'Over 30 below 35 they have a obese')
    
else:
    print(f"Above 35 they are clinically obese.")