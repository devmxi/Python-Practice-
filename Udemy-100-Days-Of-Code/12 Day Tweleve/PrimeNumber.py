def getint():
    return int(input("Give me a number: ")) #get intager function, to get an intager number

#* is prime function
def is_prime(num):
    count = -1 #* counter starting at -1 to account for 1 not being a prime number
    #fixed loop for each item in the divisors list
    for numbers in range(1, num):
        if num % numbers == 0: #*checking if its divsible by any of the numbers
            count += 1 
    if count == 0:
        return True
    else:
        return False
    
    
    
num = getint()
print(is_prime(num))
