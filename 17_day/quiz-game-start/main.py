from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [] # list: bank of questions
question_number = 0 # int: number of the question

for question in question_data: # question_data -->  list[ dict: {'text', 'answer'}]
    question_text = question['text'] # str: text
    question_answer = question['answer'] # str: answer
    new_question = Question(q_text = question_text, q_answer = question_answer) # Question object: input -> { q_text, q_answer }
    question_bank.append(new_question)

quiz = QuizBrain(q_list = question_bank) # QuizBrain object: input -> { q_list }

while quiz.still_has_questions():
    quiz.next_question() # method: input true or false from the user
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")