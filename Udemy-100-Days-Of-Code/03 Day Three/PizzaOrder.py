#conditionals practice 

#vars
size = "" #str
pepperoni = "" #str
extra_cheese = "" #str
bill = 0.0 #float

#welcome message 
print("Welcome to Python Pizza Deliveries") 

#getting user inputs 
size = str(input("What size of pizza do you want? S, M or L: "))
pepperoni = str(input("Would you like pepperoni on that? Y or N: "))
extra_cheese = str(input("Do you want extra cheese? Y or N: "))


#conditionals to check pizza size
if size == "S":
    bill += 15 #adding to bill
    
    #checking if they want pepperoni
    if pepperoni == "Y": 
        bill += 2 #adding to bill
    
elif size == "M":
    bill += 20 #adding to bill
    
    if pepperoni == "Y": 
        bill += 3 #adding to bill
        
else:
    bill += 25

    if pepperoni == "Y": 
        bill += 3 #adding to bill

#checking for extra cheese
if extra_cheese == "Y":
    bill += 1 #adding to bill
    
#output message
print(f"Your final bill is ${round(bill, 2)}")

