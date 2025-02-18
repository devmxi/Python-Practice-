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

    #TODO create a function called encrypt, that takes original text and shift amount as 2 inputs
    def encrypt(original_txt, shift_amt):
        encryptedtxt = ""
        #TODO inside the encrypt function shift each letter of the original txt forwards in the alphabet by the shift amount and print the encrypted text
        #* use .index function 
        for letters in original_txt:                                                              #TODO what happens if you try to shift z forward by 9
                encryptedtxt += alphabet[((alphabet.index(letters)) + shift_amt) % len(alphabet)] #* sets encrypted text to be the letter currently in original text, shifted by the original inputted amt. -
                                                                                                #* -then modulos that by the length of the list, as if theres a remainder it will be the needed shift amount from the start of the list  
        print(f"Here is your encoded text: {encryptedtxt}")
        
        
    #TODO Create a function called decrypt that decrypts the encrypted text 
    def decrypt(encryptedtxt, shift_amt):
        originaltxt = ""
        for letters in encryptedtxt:                                                              
                originaltxt += alphabet[((alphabet.index(letters)) - shift_amt) % len(alphabet)]
                                                                                
        print(f"Here is your decoded text: {originaltxt}")
        

    #TODO Combine encrypt and Decrypt functions into one fucntion called ceaser and use direction to determine what one to use
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


    #TODO call the Ceaser  fucntion and pass in user inputs
    ceasar(direction, text, shift)
    exit = input("Would you like to continue? True \\ False: ").lower()
    
