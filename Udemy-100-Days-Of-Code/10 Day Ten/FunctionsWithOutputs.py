# defining a function
def function():
    print("Blah..Blah..Blah")
    
#-------------------------------------------------------------------------------------------------#

#* defining a function with an output
def functionwithoutput():
    result = 3 * 2 #* does the calculation
    return result  #* will produce the output of the calculation, this can be stored to another vairable 

output = functionwithoutput()

#-------------------------------------------------------------------------------------------------#
 
#* practical usage:
def formatname(firstname, lastname):
    
    if firstname == "" and lastname == "": #* checks if the input acutally has a value
        return "Empty inputs" #! early return
     
    firstname = firstname.title() #* converts to title case eg: new york --> New York
    lastname = lastname.title()
    fullname = firstname + " " + lastname #* concatinates together
    return fullname #*outputs - return shows the end of the function

print(formatname(str(input("Please enter your first name: ")), str(input("Please enter your last name: "))))

#-------------------------------------------------------------------------------------------------#