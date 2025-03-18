from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    question_bank. append(Question(questions["text"], questions["answer"]))

quiz = QuizBrain(question_bank)

while quiz.more_questions():
    quiz.next_question()