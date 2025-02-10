#import
import random

listlen = 0
listlen = int(input("How long would you like the list to be: \n"))

list1 = random.sample(range(1, random.randint(2, 50)), listlen)
list2 = random.sample(range(1, random.randint(2, 50)), listlen)

# list1 = [1,2,3] 
# list2 = [1,4,5]

print(list1)
print(list2)

for item in list1:
    if item in list2:
        print(item)