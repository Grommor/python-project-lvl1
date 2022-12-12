from random import randint


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    question_number = randint(1, 100)
    question = (f'Question: {question_number}')
    answer = 'no'
    if 0 == (question_number % 2):
        answer = 'yes'
    return question, answer
