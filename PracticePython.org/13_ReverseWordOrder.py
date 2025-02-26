sentance = "" #input string
reversed_sentance = [] #sentance reversed in a list
output_sentance = "" #output string 

def split_string(longstring, list):
    '''splits a sentance into individual words, returns as a list'''
    list = longstring.split() 
    return list

def reverse_word_order(list, output):
    ''' adds all words in list to output string in reverse order. returns ouput string'''
    for x in range(1, len(list)+1):
        output += list[-x]
        output += " "
    return output

def get_user_input(longstring):
    '''gets user input, returns user input'''
    longstring = str(input("Please enter a sentance: "))
    return longstring
    

#output 
print(reverse_word_order(split_string(get_user_input(sentance), reversed_sentance), output_sentance))