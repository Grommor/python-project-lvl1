from random import randint

task = 'What number is missing in the progression?'


def generate_question_and_answer():
    d = randint(0, 9)
    progression_list = list(range(randint(1, 15), 150, randint(1, 10)))
    answer = str(progression_list[d])
    progression_list[d] = '..'
    question = ('Question: ' + " ".join(map(str, progression_list[0:10])))
    return question, answer
