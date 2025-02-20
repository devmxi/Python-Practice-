#
#*creating our own little peices of documentation for our functions

def formatname(firstname, lastname):
    
    '''Takes first and last names, formats it into title case and returns full, formated name''' #! docstrings have to be the first line in the function, and declared like this
    
    if firstname == "" and lastname == "": #* checks if the input acutally has a value
        return "Empty inputs" #! early return
     
    firstname = firstname.title() #* converts to title case eg: new york --> New York
    lastname = lastname.title()
    fullname = firstname + " " + lastname #* concatinates together
    return fullname #*outputs - return shows the end of the function

print(formatname(str(input("Please enter your first name: ")), str(input("Please enter your last name: "))))
#* Hover over ^ this to see docstring

#-------------------------------------------------------------------------------------------------#