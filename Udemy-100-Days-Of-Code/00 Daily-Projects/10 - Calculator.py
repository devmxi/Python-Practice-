#addition function
def addition(num1, num2):
    '''Adds two numbers together'''
    return num1 + num2 

#subtraction function
def subtraction(num1, num2):
    '''Subtracts two numbers'''
    return num1 - num2 

#multiplication function
def multiplication(num1, num2):
    '''multiplies two numbers together'''
    return num1 * num2 

#division function
def division(num1, num2):
    '''divides two numbers'''
    return num1 / num2 

#* dicitonary containing all functions as values for specific operator keys, allowing them to be called
operators = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    
}

#assigning vars
morecalculations = "" #string 
operation = "" #string
calculations = 0 #int

#while loop, goes unti user wants to exit
while morecalculations != "exit":
    
    if morecalculations == "y": #* checks if the user has previously inputed that they want to continue with the calculations 
        num1 = total #* sets num 1 to total if true 
    else:
        print('\n')*20
        num1 = float(input("What's the first number: ")) #asks for user input 
        
    for signs in operators:#* ouputs all operators 
        print(signs)
    
    operation = input("Please pick what operation you would like to use: ") #asks for input
    
    num2 = float(input("What's the next number: ")) #asks for input
    
    total = operators[operation](num1, num2) #* goes to key of inputed value, then runs function at value of key 
    calculations += 1 #increases calc
    print(f"{num1} {operation} {num2} = {total}") #*outputs calculation
    morecalculations = str(input(f"type 'y' to continue calculating with {total}, type 'n' to start a new calculation, or type 'exit' to exit: ")).lower() #*asks user next steps
    
print(f"Thank you for using the calculator, you completed {calculations} calculations") #* final output of total calculations completed