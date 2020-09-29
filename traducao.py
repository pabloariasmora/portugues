from misc import open_csv, validate_answer
import random
from colorama import Fore, Back, Style

questions = open_csv('traducao.csv')

# Random
random.shuffle(questions)

general_question = 'Qual é a tradução?'

total = len(questions)
good = 0
bad = 0

for row in questions:
    print(Fore.BLUE + general_question + Style.RESET_ALL)

    num = random.randint(0, 100)
    if num > 50:
        print("Português")
        a = row[0]
        b = row[1]
    else:
        print("Espanhol")
        a = row[1]
        b = row[0]

    print(a)

    invalid_anwer = True
    while invalid_anwer:
        try:
            answer = input("reponda: ")
            invalid_anwer = False
        except UnicodeDecodeError:
            print("erro de leitura")
            invalid_anwer = True

    response = validate_answer(answer, b)
    if response:
        good = 1 + good
    else:
        bad = bad + 1
    print('T[{}]:'.format(total)+Fore.GREEN + 'S[{}]:'.format(good)+Fore.RED + 'F[{}]'.format(bad) + Style.RESET_ALL)
    print('-------------------')