from question_model import Question
from data import question_data
from quiz_brain import Quiz
import requests

print("Begin")
question_bank = []
for record in question_data:
    record_text = record['text']
    record_ans = record['answer']
    question_bank.append(Question(record_text,record_ans))


quiz_obj = Quiz(question_bank)

while quiz_obj.has_next_question():
    quiz_obj.next_question()

print("Your Quiz is completed")
print(f"Your final score is {quiz_obj.score}/{quiz_obj.question_index}")

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
print(response.status_code)
print(response.json())