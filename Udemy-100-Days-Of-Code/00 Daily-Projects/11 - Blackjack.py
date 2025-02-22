import random #*importing module 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #* array of all avalible cards
playgame = "y" #* setting wanting to play next game to true 
cardorpass = "" #* wanting to draw another card 
gamecounter = 0 #* amt of times game has been played
score = 0.0 #* score, +1 if win +.5 if draw -1 if loss


def calcscore(cards):
    '''loops for each item in a list, caclulating the total of the whole list. Returns total'''
    totalscore = 0
    for item in cards:
        totalscore += item
    return totalscore

def ouputfinalscore():
    '''Outputs final message of scores.'''
    print(f"\t Your final hand: {usercards}, final score: {calcscore(usercards)}")
    print(f"\t Computer's final hand: {computercards}, final score: {calcscore(computercards)}")
    
def acevalue(deck):
    '''Checks if the ace is in their deck, if it is and would make them go over 21, it is converted to a 1'''
    if 11 in deck and calcscore(deck) > 21:
       deck[deck.index(11)] = 1

def newcard(condition):
    '''checks if user wants a new card, if they do it adds one to their deck and checks if its an ace. If they dont it will do the same for the computer'''
    if condition == "y":
        usercards.append(random.choice(cards))
        acevalue(usercards)
        
    else:
        computercards.append(random.choice(cards))
        acevalue(computercards)
        #*chekcing if dealers value is 16 or less, so they have to take another card
        while calcscore(computercards) <= 16:
            computercards.append(random.choice(cards))
            acevalue(computercards)

print("Welcome to BlackJack. Here is the scoring: \n Win: +1 \n Tie: +0.5 \n Loss: - 1 \n")
while playgame == "y": #*while they want to play the game the code will loop
    
    playgame = str(input("Would you like to play a game of BlackJack? Type 'y' or 'n': ")).lower() #* asks for user input if theyd like to play blackjack
    #*input validation
    
    while playgame != "y" and playgame != "n":
        playgame = str(input("Error, please enter 'y' or 'n': ")).lower()
    
    if playgame == 'n': #* checks if not, then breaks loop
        break
    
    if gamecounter > 0: #* checks if theyve played a previous game, if yes, itll clear screen.
            print('\033c')
            
    #* generates random deck 
    usercards = [random.choice(cards)]
    usercards.append(random.choice(cards))
    acevalue(usercards)
    computercards = [random.choice(cards)]
    
    #* loops for both cards not equalling 21
    while calcscore(usercards) < 21 and calcscore(computercards) < 21:
        
        #* tabs in and shows users current cards, and the computers first card
        print(f"\t Your cards: {usercards}, current score: {calcscore(usercards)}")
        print(f"\t Computer's first card: {computercards[0]}")
        
        #* asks if they want another card
        cardorpass = str(input("Type 'y' to get another card, type 'n' to pass: ")).lower()
        
        #*Input validation
        while cardorpass != "y" and cardorpass != "n":
            cardorpass = str(input("Error, please enter 'y' or 'n': ")).lower()
        
        newcard(cardorpass) #*using function to check conditional
        
        #* checks if because of the new card theyve gone over 20 
        if calcscore(usercards) > 21:
            break
        elif cardorpass == "n": #* checks if they passed their turn
            break

    #* if they went over 21, then they loose 
    if calcscore(usercards) > 21: 
        ouputfinalscore()
        print("\t You went over 21. You loose.")
        gamecounter += 1
        score -= 1 #*loosing one point
    
    #*all possible win conditions for user 
    elif calcscore(usercards) > calcscore(computercards) or calcscore(computercards) > 21: 
        ouputfinalscore()
        print("\t you win")
        gamecounter += 1
        score += 1
        
    #* checks for tie
    elif calcscore(usercards) == calcscore(computercards):
        ouputfinalscore()
        print("\t Its a tie")
        gamecounter += 1
        score += 0.5
    
    #* if they didnt win, and its not a tie, and they didnt go over, they lose 
    else:
        ouputfinalscore()
        print("\t You loose")
        gamecounter += 1
        score -= 1

#* final output if they dont wish to continue
print(f"Thank you for playing! You played {gamecounter} games, and you ended with a score of {score}")

#11/100 - thought this project would be harder ngl