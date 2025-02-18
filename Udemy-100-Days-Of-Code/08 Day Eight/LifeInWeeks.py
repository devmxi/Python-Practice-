#
#* Program to caclulate life in weeks from users age till they hit 90

def life_in_weeks(age):
    time_left = ((90 - age)*364)//7 #calculate weeks left
    print(f"You have {time_left} weeks left.") #prints
    
life_in_weeks(int(input("How old are you: "))) #asks for input