from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
INTERVAL_START = 1
INTERVAL_END = 100


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    for i in range(2, int(number / 2) + 2):
        if number % i == 0:
            return False
    return True


def generate_question_and_answer():
    question_number = randint(INTERVAL_START, INTERVAL_END)
    question = (f'Question: {question_number}')
    answer = 'no'
    if is_prime(question_number):
        answer = 'yes'
    return question, answer
