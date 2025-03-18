#importing modules
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [] #* initalising an array 

for questions in question_data: #* loops for every key in dicitionary
    question_bank. append(Question(questions["question"], questions["correct_answer"])) #* creates a question obj, assigns it to array

quiz = QuizBrain(question_bank) #* creates quizbrain obj

while quiz.more_questions(): #*checking if more questions exist
    quiz.next_question() #* asks next question
    
print(f"Youve completed the quiz! \nYour final score was:{quiz.score}/{quiz.question_number}") #* final output