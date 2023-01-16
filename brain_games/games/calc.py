from random import randint, choice

TASK = 'What is the result of the expression?'
INTERVAL_START = 1
INTERVAL_END = 100
ARITHMETIC_SIGNS = ['+', '-', '*']


def generate_question_and_answer():
    operation_sign = choice(ARITHMETIC_SIGNS)
    member_1 = randint(INTERVAL_START, INTERVAL_END)
    member_2 = randint(INTERVAL_START, INTERVAL_END)
    if operation_sign == '+':
        result = member_1 + member_2
    elif operation_sign == '-':
        result = member_1 - member_2
    elif operation_sign == '*':
        result = member_1 * member_2
    question = f'Question: {member_1} {operation_sign} {member_2}'
    result = str(result)
    return question, result
