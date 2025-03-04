import random

number = 0
#how random can i make something? 
def rand_num(num): 
    num = random.randint(0,100)
    return num
    
def even_odd_randomiser(num):
    if num % 2 == 0:
        num *= random.randint(0,50)
    else:
        num *= random.randint(51,100)  
    return num

def higher_lower(num):
    if num < 100: 
        num += random.randint(0,50)
    else:
        num -= random.randint(0,50)
    return num

print(higher_lower(even_odd_randomiser(rand_num(number))))
