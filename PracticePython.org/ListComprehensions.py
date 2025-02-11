#vars
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] #provided list 
evenNum = [0] #even num list

for i  in list:
    if i % 2 == 0: #checks if number is even 
        evenNum.append(i) #adds to new list 
        
print(evenNum) #prints list 