def minmaxlist(list): #* defining the function
    newlist=[]
    newlist.append(list[0]) #* adding first item of inputted list to a new list 
    newlist.append(list[-1])#* adding last item of inputted list to a new list 
    return newlist #*returning whole of new list 

a_list = [5, 10, 15, 20, 25]

print(minmaxlist(a_list)) #*output