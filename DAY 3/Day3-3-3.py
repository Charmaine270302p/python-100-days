print("\033c")

#DAY3-3 Challenge(leap year)
year = int(input('Which year do you want to check?'))

if year % 4 == 0:
    print('This is a leap year.')

elif year % 100 == 0:
   print('Its a leap year.')
      
elif year % 400 == 0:
    print('Leap year.')
    
else:
    print("Not a leap year.")
    
    
# if year % 4 == 0:
#    if year % 100 == 0:
#         if year % 400 == 0:
#             print('leap year.')
#         else:
#             print('Not a leap year.')
#     else:
#         print(' a leap year.')
# else:
#     print('Not a leap year.')