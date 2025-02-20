def is_leap_year(year):
    ''' Takes a year as an input and checks if it is a leap year or not''' #! docstring
    leap = True
    
    if year % 4 == 0: #* checking if year is divisble by 4 
        leap = True 
    else: 
        leap = False #* if not its false 
        
    if year % 100 == 0: #* checking if year is divisble by 100
        leap = False
        
    if year % 400 == 0: #* checking if year is divisble by 400
        leap = True
                
    return leap #* returning output

print(is_leap_year(int(input("year: "))))