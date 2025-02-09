#var
num = 0 #int
x = 0 #int 


num = int(input("Please enter a positive number"))

while num < 0 :
    num = int(input("Error! Please enter a postiive number"))

x = int(input("Please enter another positive number"))

while x < 0 :
    x = int(input("Error! Please enter a postiive number"))

if num % x == 0:
    print(x, "divides evenly into", num)
else:
    print(x, "does not evenly divide into", num)

if num % 4 == 0: 
    print(num , " is an even number, and a multiple of four")
elif num % 2 == 0:
    print(num, " is an even number")
else: 
    print(num, "is an odd number")