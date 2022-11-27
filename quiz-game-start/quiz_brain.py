from question_model import Question
from data import question_data


class Quiz:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_index = 0
        self.score = 0

    def has_next_question(self):
        return self.question_index < len(self.question_list)

    def check_answer(self, user_answer, q_answer):
        if user_answer == q_answer:
            self.score += 1
            print(f"You got it Buddy. Your score is {self.score}/{self.question_index}")
        else:
            print(f"Oops Wrong Answer. Your score is {self.score}/{self.question_index}")
        print("")

    def next_question(self):
        question = self.question_list[self.question_index]
        self.question_index += 1
        user_ans = input(f"Q:{self.question_index}. {question.text} (True/False): ")
        self.check_answer(user_ans, question.answer)
