from misc import open_csv, validate_answer
import random
from colorama import Fore, Back, Style

questions = open_csv('artigos.csv')

# Random
random.shuffle(questions)

general_question = 'Qual é o artigo desta palavra?'

total = len(questions)
good = 0
bad = 0
for row in questions:
    print(Fore.BLUE + general_question + Style.RESET_ALL)
    print(row[0])
    answer = input("reponda: ")
    response = validate_answer(answer, row[1])
    if response:
        good = 1 + good
    else:
        bad = bad + 1
    print('T[{}]:'.format(total)+Fore.GREEN + 'S[{}]:'.format(good)+Fore.RED + 'F[{}]'.format(bad) + Style.RESET_ALL)
    print('-------------------')



