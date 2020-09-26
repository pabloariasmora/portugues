from misc import open_csv, validate_answer
import random

questions = open_csv('artigos.csv')

# Random
random.shuffle(questions)

general_question = 'Qual é o artigo desta palavra?'

for row in questions:
    print(general_question)
    print(row[0])
    answer = input("reponda: ")
    validate_answer(answer, row[1])
    print('-------------------')

