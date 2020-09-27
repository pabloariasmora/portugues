import csv
from colorama import Fore, Back, Style

def open_csv(filename='artigos.csv'):
    contents = []
    with open(filename, newline='') as csvfile:
        filecontents = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in filecontents:
            contents.append(row)

    return contents


def validate_answer(answers, valid_answers):
    # Enter is valid as -
    if not answers:
        answers = "-"

    if not "+" in valid_answers:
        # Single Answer
        valid_answers_list = valid_answers.split('|')
        valid = False
        for valid_answer in valid_answers_list:
            if valid_answer.strip().lower() == answers.strip().lower():
                valid = True
                break
        if valid:
            print(Fore.GREEN + 'Certo' + Style.RESET_ALL)
        else:
            print(Fore.RED + 'Incorreta:' + Style.RESET_ALL)
            print(" ,".join(valid_answers.split("|")))
    else:
        # Multiple answers required
        answers = answers.split(" ")
        valid_answers = valid_answers.split("+")

        if len(answers) == len(valid_answers):

            valid=True
            for answer, valid_answer in zip(answers, valid_answers):
                if not valid_answer.strip().lower() == answer.strip().lower():
                    valid = False
        else:
            valid = False

        if valid:
            print(Fore.GREEN + 'Certo' + Style.RESET_ALL)
        else:
            print(Fore.RED + 'Incorreta:' + Style.RESET_ALL)
            print(" ".join(valid_answers))

    return valid
