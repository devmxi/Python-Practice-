bids = {} #new dictionary
more_bids = "true" #setting to true automatically 
art = ''' 

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         |_________|
                         `'-------'`
                       .-------------.
                      |_______________|
                          
        '''
        

    
print(art) 
print("Welcome to the silent auction") #printing welcome message

while more_bids == "true":  #loops until they say stop 
    name = str(input("Please enter your name: ")) #asking for user name 
    bid  = int(input("Please enter your bid: £")) #asking for user bid 
    bids[name] = bid #making new key: value in dictionary
    
    more_bids = str(input("Is there more bidders? True/False: ")).lower() #checking if they want to add more bidders 
    if more_bids == "true": 
        print("\n"*100) #`clearing` console 
        
def finding_heighst_bidder(dictionary):
    heighstbid = 0
    heighestbidder = ""
    #checking each key in dictionary for heighst bidder 
    for people in bids:
        if bids[people] > heighstbid:
            heighstbid = bids[people] 
            heighestbidder = people
            
    print(f"The highest bidder is {heighestbidder}, who bid £{heighstbid}")
    
    
#output          
finding_heighst_bidder(bids)


#9/100 - Nearly at day 10!!