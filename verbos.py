from misc import open_csv, validate_answer
import random
from colorama import Fore, Back, Style

questions = open_csv('verbos.csv')



general_question = 'Qual é a conjugação?'

persons = questions[0]
questions = questions[1:]
# Random
random.shuffle(questions)
for row in questions:
    person = random.randint(1, len(persons)-1)
    print(Fore.BLUE + general_question + Style.RESET_ALL)
    # Format person if more than one
    if "|" in persons[person]:
        person_list = persons[person].split("|")
        random.shuffle(person_list)
        print(person_list[0] + ' (' + row[0] + ')')
    else:
        print(persons[person] + ' (' + row[0] + ')')
    answer = input("Reponda: ")
    validate_answer(answer, row[person])

    print('-------------------')

