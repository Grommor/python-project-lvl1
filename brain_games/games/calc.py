from random import randint


task = 'What is the result of the expression?'


def generate_question_and_answer():
    c = randint(0, 100)
    d = randint(0, 100)
    match randint(0, 2):
        case 0:
          answer = str(c + d)
          question = (f"Question: {c} + {d}:")
        case 1:
          if c >= d:
            answer = str(c - d)
            question = (f"Question: {c} - {d}:")
          else:
            answer = str(d - c)
            question = (f"Question: {d} - {c}:")
        case 2:
            answer = str(c * d)
            question = (f"Question: {c} * {d}:")
    return question, answer

