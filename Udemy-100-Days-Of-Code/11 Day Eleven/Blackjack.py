import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playgame = "y"
cardorpass = "y"

def calcscore(cards):
    totalscore = 0
    for item in cards:
        totalscore += item
    return totalscore

def ouputfinalscore():
    print(f"\t Your final hand: {usercards}, final score: {calcscore(usercards)}")
    print(f"\t Computer's final hand: {computercards}, final score: {calcscore(computercards)}")
    
def acevalue(deck):
    if 11 in deck and calcscore(deck) == 21:
       deck[deck.index(11)] = 1

def newcard(condition):
    if condition == "y":
        usercards.append(random.choice(cards))
        acevalue(usercards)
        
    else:
        computercards.append(random.choice(cards))
        acevalue(computercards)

while playgame == "y":
    playgame = str(input("Would you like to play a game of BlackJack? Type 'y' or 'n': ")).lower()
    
    if playgame == 'n':
        break
    
    usercards = [random.choice(cards), random.choice(cards)]
    computercards = [random.choice(cards)]
    
    while calcscore(usercards) < 21 and calcscore(computercards) < 21:
        print(f"\t Your cards: {usercards}, current score: {calcscore(usercards)}")
        print(f"\t Computer's first card: {computercards[0]}")
        
        cardorpass = str(input("Type 'y; to get another card, type 'n' to pass: ")).lower()
        
        newcard(cardorpass)
        
        if calcscore(usercards) > 21:
            break
        elif cardorpass == "n":
            break
     
    if calcscore(usercards) > 21: 
        # while calcscore(computercards) < calcscore(usercards):
        #     computercards.append(random.choice(cards))
        ouputfinalscore()
        print("\t You went over 21. You loose.")
        
    elif calcscore(usercards) > calcscore(computercards):
        ouputfinalscore()
        print("\t you win")
        
    elif calcscore(usercards) == calcscore(computercards):
        ouputfinalscore()
        print("\t Its a tie")
        
    else:
        ouputfinalscore()
        print("\t You loose")
