import prompt

ROUNDS = 3


def user_welcome():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def check_answer(answer, question):
    print(question)
    client_answer = prompt.string('Your answer: ', empty=True)
    if answer == client_answer:
        print('Correct!')
    else:
        user_bye(client_answer, answer)


def user_bye(answer=0, right_answer=0, win=0):
    if win:
        print(f'Congratulations, {name}!')
        exit()
    else:
        print(f'\'{answer}\' is wrong answer ;(. \
Correct answer was \'{right_answer}\'.')
        print(f'Let\'s try again, {name}!')
        exit()


def run_game(game):
    user_welcome()
    print(game.TASK)
    for i in range(ROUNDS):
        question, answer = game.generate_question_and_answer()
        check_answer(str(answer), question)
    user_bye(win=True)
