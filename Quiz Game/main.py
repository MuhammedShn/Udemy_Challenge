from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    question_bank.append(Question(q_text, q_answer))

quiz = QuizBrain(question_bank)

quiz.question_number = 0
while quiz.still_has_question():
    quiz.next_question()
