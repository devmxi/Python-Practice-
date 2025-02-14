#fixed loops \\ for loops 
# loops that loop for a ceritan range

fruits = ["Apples", "Grapes", "Bananas"]

for fruit in fruits: #give keyword to item, and then in and then list 
    #* what it does is fruit is a variable, then it sets it to the one corresponding to it in the array: first loop = 0 first item = apples 
    print(fruit)
    
#-------------------------------------------------------------------------------------------------#

#* In built function sum
student_score = [190, 124, 182, 145, 156, 127]

totalscore = sum(student_score) #adds up all the values in student score
print(totalscore)

#* The equivelant is 
totalscore = 0

for score in student_score:
    totalscore += score

print(totalscore)

#-------------------------------------------------------------------------------------------------#

#* In built function max 
student_score = [190, 124, 182, 145, 156, 127]

highest_score = max(student_score) #gets the highest value in an array
print(highest_score)

#* The equivelant is 
highest_score  = 0

for score in student_score:
    if score > highest_score:
        highest_score = score
        
print(highest_score)

#-------------------------------------------------------------------------------------------------#

# for loops independedntly of lists
#* using range 
sequence = 0  #1 + 2 + 3 ... + 98 + 99 + 100 \\ the gauss challange 

for num in range(1, 101):
    sequence = sequence + num  #*Keeping a running total
    
print(sequence)
