class QuizBrain: #* new class for the quiz logic
    
    def __init__(self, questions_list): #* new attrabute called question list
        self.score = 0
        self.question_number = 0 
        self.questions_list = questions_list #* setting the attrabute to paramaters
        
    #TODO: check if were at the end of the quiz 
    def more_questions(self): #* model (function)
        return self.question_number < len(self.questions_list) #* checks the condition, if true it returns true
    
    #TODO: ask questions
    def next_question(self):#* model (function)
        
        current_question = self.questions_list[self.question_number] #* assigns current question to a variable from array
        self.question_number += 1 #* accounts for lists starting at 0
        
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ") #* asks question
        self.check_answer(user_answer, current_question.answer) #* checks answer from user input
        
    #TODO: check if answer was correct 
    def check_answer(self, user_input, question_answer):#* model (function)
        
        if user_input.lower() == question_answer.lower(): #* checks if user answer matches with correct answer
            self.score += 1
            print(f"You got it right! Current Score: {self.score} / {self.question_number}") #* score output
        else:
            print(f"You got it wrong! Current Score: {self.score} / {self.question_number}")#* score output
            print(f"The corrct answer was {question_answer}")
        
        print("\n") #* new line