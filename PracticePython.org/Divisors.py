#var 
num = 0 #int 
num = int(input("Please enter the number youd like to see all the divisors of: \n")) #asks for input and assgins it to the variable 

#dec range with the max range of input 
divisorRange = range(1, num)

#fixed loop - range is the list defined in prev line 
for i in divisorRange:
    if num % i == 0: #checking if num is divisible by each number in the range
        print(i) #outputting 

