
#TODO: ask questions

#TODO: check if answer was correct 

#TODO: check if were at the end of the quiz 

class QuizBrain:
    
    def __init__(self, questions_list):
        self.score = 0
        self.question_number = 0 
        self.questions_list = questions_list
        
    def more_questions(self):
        return self.question_number >= len(self.questions_list) #* checks the condition, if true it returns true
    
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_input, question_answer):
        
        if user_input.lower() == question_answer.lower():
            self.score += 1
            print(f"You got it right! Current Score: {self.score}")
        else:
            print(f"You got it wrong")
            print(f"The corrct answer was {question_answer}")