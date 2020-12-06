from sys import argv
from os import chdir


def first_part(data):
    set_answers = set()
    answers_group = 0
    for line_i in range(len(data)):
        if data[line_i] != '':
            set_answers = set(data[line_i]).union(set_answers)
        else:
            answers_group += len(set_answers)
            set_answers = set()

        if line_i == len(data) - 1:
            answers_group += len(set_answers)

    return answers_group


def second_part(data):
    set_answers = set(data[0])
    answers_group = 0
    for line_i in range(len(data)):
        if data[line_i] != '':
            set_answers = set(data[line_i]).intersection(set_answers)
        else:
            answers_group += len(set_answers)
            set_answers = set(data[line_i + 1])

        if line_i == len(data) - 1:
            answers_group += len(set_answers)

    return answers_group


def day_6_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    input_data = open(path_to_input, 'r').readlines()
    input_data = [input_data[i].rstrip() for i in range(len(input_data))]

    answer_1 = first_part(input_data)
    answer_2 = second_part(input_data)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_6_solution(input_folder_name, input_file_name)