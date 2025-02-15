#Conditional loops
#infinite loops until the requirement changes to false
#* WHEN TO USE THEM: WHEN YOU DONT CARE ABOUT THE ITEMS IN A LIST

countdown = 10

while countdown != 0: #*while loop until it hits 0
    print(f"New Years in: {countdown}") #prints 
    countdown -= 1 #subtracts 1 from countdown
    
print("Happy New Year!!")

#-------------------------------------------------------------------------------------------------#

#* hurdles task with while loop (2)
# hurdles = 6 

#def turn_right(): #* def function
    #turn_left()
    #turn_left()
    #turn_left()
    
#def hurdle(): #* def function
    #move()
    #turn_left()
    #move()
    #turn_right()
    #move()
    #turn_right() #*calls previous function
    #move()
    #turn_left() 

#while hurdles != 0: #*while hurdles(var) doesnt = 1
#   hurdle() #*calls function
#   hurdles -= 1 #* subtracts from hurdles

#-------------------------------------------------------------------------------------------------#

#* Harder Hurdles Task (3)
#def turn_right(): #* def function
    #turn_left()
    #turn_left()
    #turn_left()
    
#def hurdle(): #* def function
    #turn_left()
    #move()
    #turn_right()
    #move()
    #turn_right() #*calls previous function
    #move()
    #turn_left() 
    
#while not at_goal():
    #if front_is_clear(): #* if the front is clear
        #while front_is_clear(): #*repeat forever if the wall is clear, then move
            #move()
    #else: #* once its not clear, jump
        #hurdle()
#-------------------------------------------------------------------------------------------------#

#*HARDEST HURDLE TASK (4)

#def turn_right():
    #turn_left()
    #turn_left()
    #turn_left()

#def goup():
    #turn_left()
    #move()
#def godown():
    #move()
    

#while not at_goal():
    #if front_is_clear() and not right_is_clear():
        #while front_is_clear() and not right_is_clear():
            #move()
    #elif not front_is_clear() and not right_is_clear():
        #turn_left()
        #if not front_is_clear() and not right_is_clear():
            #goup()
   # else:
        #while right_is_clear():
            #turn_right()
            #godown()
            
#-------------------------------------------------------------------------------------------------#