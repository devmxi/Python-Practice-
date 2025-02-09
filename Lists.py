a = [1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
req = 0 

req = int(input("What numbers from the original list would you like it to print less than: " ))
print( [i for i in a if i < req])
                    # ^^--- does what the bottom two lines in one line, 
#for i in a:           # ---> For loop for an array, in this instant each loop I will be the value of the corresponding array slot 
    #if i < 5:print(i) # ---> Prints if its less than 5 



