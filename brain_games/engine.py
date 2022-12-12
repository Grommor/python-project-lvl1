import brain_games.cli as cli

rounds = 3

def run_game(game):
    cli.user_welcome()
    print(game.task)
    for i in range(rounds):
        question, answer = game.generate_question_and_answer()
        cli.check_answer(str(answer), question)
    cli.user_bye(win=True)


