#var
num = 0 #int
x = 0 #int 


num = int(input("Please enter a positive number: ")) #assigning value to var and asking for input 

#input validation 
while num < 0 :
    num = int(input("Error! Please enter a postiive number: ")) #error message output 

x = int(input("Please enter another positive number: ")) #assigning value to var and asking for input 

#input validation 
while x < 0 :
    x = int(input("Error! Please enter a postiive number: ")) #error message output 


#proccesses / outputs 
#checking if num evenly divides into x 
if num % x == 0:
    print(x, "divides evenly into", num) #output 
else:
    print(x, "does not evenly divide into", num) #output 

#checking if num is a multiple of four 
if num % 4 == 0: 
    print(num , " is an even number, and a multiple of four") #output 
elif num % 2 == 0: #checking if num is even 
    print(num, " is an even number") #output 
else: #if not even, it has to be odd 
    print(num, "is an odd number") #output 