from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
INTERVAL_START = 1
INTERVAL_END = 100


def generate_question_and_answer():
    question_number = randint(INTERVAL_START, INTERVAL_END)
    question = (f'Question: {question_number}')
    answer = 'no'
    if 0 == (question_number % 2):
        answer = 'yes'
    return question, answer
