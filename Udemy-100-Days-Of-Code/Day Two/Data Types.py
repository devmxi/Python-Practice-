#* strings - text 

string = "Hello"
print(string[0]) #subscripting, printing the first character in the string // negative numbers are usable, eg: -1 is the same as the last characcter 
print(len("1234")) #len function will only work on STRINGS 

#-------------------------------------------------------------------------------------------------# 

#*intagers - whole numbers
intager1 = 123
intager2 = 345 
print(intager1 + intager2) #prints mathmatical output of 123 + 345 

print(123_456_789) #with large numbers, you are able to put underscores to increase readability, this doesnt effect output: 123456789

#-------------------------------------------------------------------------------------------------# 

#*float // real - decimal numbers

pi = 3.14159265 # stored using mantissa and exponenet 
print(pi)

#-------------------------------------------------------------------------------------------------# 

#* boolean - true / false 

yes = True
print(yes)

#-------------------------------------------------------------------------------------------------# 

#* How to figure out what datatype something is? 
#* Theres a predefined function! - used for typechecking 

print(type("Hello")) #output: String
print(type(123))     #output: Int
print(type(123.321)) #output: Float
print(type(True))    #output: Bool

#-------------------------------------------------------------------------------------------------# 

#* Type Casting 

int("123") #converts a string into an integer, this will NOT work for letters: VALUE ERROR
float()
str()
bool()

#* all convert into their respective data types 

#-------------------------------------------------------------------------------------------------# 

print("Number of letters in your name: ", len(str(input("Enter your name: \n"))))