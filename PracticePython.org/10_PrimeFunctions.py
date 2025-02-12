#declaring functions 
def getint():
    return int(input("Give me a number: ")) #get intager function, to get an intager number

#is prime function
def isprimenum(x):
    
    for i in divisorRange: #checks for number in array from 2 to number inputted 
        if x % i == 0: #checks if divisible with no remainder (therfore not prime) 
            print(f"{x} is not a prime number") #output message
            break #ends loop
        else:
            print(f"{x} is a prime number") #Output message
            break #ends loop
            
    return

num = getint() #num is set to get input function 
divisorRange = range(2, num -1 ) #range from 2 - num-1  as all prime numbers are divisble by itself and one 

isprimenum(num) #using function to output message