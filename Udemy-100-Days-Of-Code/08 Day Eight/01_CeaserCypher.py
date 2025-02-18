alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
direction = str(input("Type `encode` to encrypt, type `decode` to decrypt: \n")).lower()
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

#TODO call the encrypt fucntion and pass in user inputs
encrypt(text, shift) 