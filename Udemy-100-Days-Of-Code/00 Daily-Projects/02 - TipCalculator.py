#11/2/25

#vars
totalBill = 0.0 #float 
tip = 0  #int
partySize = 0 #int 
finalPrice = 0.0 #float 

print("Welcome to the tip calculator!\n") #ouput welcome message
totalBill = float(input("What was the total bill? £")) #getting user input for total bill cost 
tip = int(input("How much of a tip would you like to give? 10, 12, or 15? ")) #getting user input for tip

#input validation 
while tip != 10 and tip != 12 and tip != 15:
    print("Please enter a value that is 10, 12 or 15: ")

partySize = int(input("How many people should split the bill? ")) #getting user input of how many people were there

#calculation
finalPrice = round(((tip / 100 * totalBill + totalBill) / partySize), 2) 

#output 
print(f"Each person should pay: £{finalPrice}")

#2/100 - YAAAAAAAAAAY