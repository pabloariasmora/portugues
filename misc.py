import csv


def open_csv(filename='artigos.csv'):
    contents = []
    with open(filename, newline='') as csvfile:
        filecontents = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in filecontents:
            contents.append(row)

    return contents


def validate_answer(answer, valid_answers):
    valid_answers_list = valid_answers.split('|')
    valid = False
    for valid_answer in valid_answers_list:
        if valid_answer.strip().lower() == answer.strip().lower():
            valid = True
            break
    if valid:
        print('Certo')
    else:
        print('Incorreta')
