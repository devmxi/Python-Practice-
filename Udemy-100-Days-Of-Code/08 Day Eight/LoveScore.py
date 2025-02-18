
def calculate_love_score(name1, name2):
    score1 = 0
    score2 = 0
    for letters in "true":
        score1 += (name1.lower()).count(letters)
        score1 += (name2.lower()).count(letters)
    
    for letters in "love":
        score2 += (name1.lower()).count(letters)
        score2 += (name2.lower()).count(letters)
    
    print(f"{str(score1)}{str(score2)}")
    
calculate_love_score("Moksh Nanwani", "Amelia Byrne") #*together, forever