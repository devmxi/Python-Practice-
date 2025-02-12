#addition + subtraction 
print(1 + 2)
print(2 - 1)

#multiplication / powers 
print(2 * 3)
print(2 ** 3) #* to the power of: 2^3 

#division
print(5 / 2) #! always gives float
print(5 // 2) #* prints it as an intager! 

#modulo 
print(5 % 2) #prints remainder 

#-------------------------------------------------------------------------------------------------# 

# B.O.D.M.A.S [Left -> Right]
# ()
# **
# * OR / OR //
# + OR - 

print(3 * 3 + 3 / 3 - 3) #! This outputs 7
print((3 + 3) * 3 / 3 - 3 ) #* This outputs 3

#-------------------------------------------------------------------------------------------------# 

#activity

bmi = 54.5 / 1.77 ** 2 
print(int(bmi)) #flooring it to the lowest whole number

print(round(bmi, 2)) #* Rounding predefined function, (var, digits to round to)

#-------------------------------------------------------------------------------------------------# 

#assignment operator 
score = 0 

score += 1 #is equal to one more than it was previously 
print(score)

score += 1 #is equal to one more than it was previously 
print(score)

#-------------------------------------------------------------------------------------------------# 

#F-strings
print(f"Your score is {score}") #* automatically converts variables into the needed data type to print 