alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
exit = ''
print('''`                         
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88         ''')
print("")

while exit != 'false':
    
    direction = input("Type `encode` to encrypt, type `decode` to decrypt: \n").lower()
    text = str(input("Type your message: \n")).lower()
    shift = int(input("Type your shift number: \n"))
    
    def ceasar(encodeordecode, message, shiftamount):
        outputtxt = ""
        
        if encodeordecode == 'decode':
                shiftamount *= -1
                
        for letter in message:
            if letter in alphabet:       
                outputtxt += alphabet[((alphabet.index(letter)) + shiftamount) % len(alphabet)]
            else:
                outputtxt += letter

        print(f"Here is your {encodeordecode}d text: {outputtxt}")


    ceasar(direction, text, shift)
    exit = input("Would you like to continue? True \\ False: ").lower()
    
