import random
#* define a class using the `class` keyword followed by a name

class User:
    def __init__(self, username): #* creating attrabutes
        print("new user being made...")
        self.id = random.randint(1,9999)  #* setting so that inserted paramater is equal to id 
        self.username = username #* setting so that inserted param is equal to username
        self.followers = 0
        self.following = 0 
    
    def follow(self, user): #* creating a method
        user.followers += 1
        self.following += 1
        
         
user1 = User("mxi") #* assigning params
user2 = User("dev")

user1.follow(user2) #* user1 follows user 2 

print(f"Username: {user1.username} | Followers: {user1.followers} Following: {user1.following}")
print(f"Username: {user2.username} | Followers: {user2.followers} Following: {user2.following}")