from misc import open_csv, validate_answer
import random
from colorama import Fore, Back, Style

questions = open_csv('preposicao.csv')

# Random
random.shuffle(questions)

general_question = 'Complete com a preposiçâo, artigo e/ou contrações:'

total = len(questions)
for row in questions:
    print(Fore.BLUE + general_question + Style.RESET_ALL)
    print(row[0])
    answer = input("reponda: ")
    validate_answer(answer, row[1])

    print()
    print('-------------------')
