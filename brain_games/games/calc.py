from random import randint

task = 'What is the result of the expression?'


def generate_question_and_answer():
    c = randint(0, 100)
    d = randint(0, 100)
    e = randint(0, 2)
    if e == 0:
        answer = str(c + d)
        question = (f"Question: {c} + {d}:")
    elif e == 1:
        answer = str(c - d)
        question = (f"Question: {c} - {d}:")
    elif e == 2:
        answer = str(c * d)
        question = (f"Question: {c} * {d}:")
    return question, answer
