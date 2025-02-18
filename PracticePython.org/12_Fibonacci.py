#creating the fibonacci sequence
def fibonacci(rangenum): #defining function
    prevnum1 = 0 #assigning first value to be 0 
    prevnum2 = 1 #assigning second value to be 1 
    for x in range(rangenum): #fixed loop with user-inputted range
        total = prevnum1 + prevnum2 #calculating the total 
        if x % 2 != 0: #flip flopping between even and odd nums to decide what one is now the previous num
            prevnum1 = total #assigning
        else:
            prevnum2 = total #assigning
        print(total) #output

fibonacci(int(input("How many digits would you like the fibonacci sequence to: "))) #getting user input