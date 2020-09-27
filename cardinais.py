from misc import open_csv, validate_answer
import random
from colorama import Fore, Back, Style

questions = open_csv('cardinais.csv')

# Random
random.shuffle(questions)

general_question = 'Que numero é esse?'


for row in questions:
    print(Fore.BLUE + general_question + Style.RESET_ALL)
    print(row[0])

    invalid_anwer = True
    while invalid_anwer:
        try:
            answer = input("reponda: ")
            invalid_anwer = False
        except UnicodeDecodeError:
            print("erro de leitura")
            invalid_anwer = True

    validate_answer(answer, row[1])
    print('-------------------')

