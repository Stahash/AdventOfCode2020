from sys import argv
from os import chdir


def sum_exists(data, value):

    existence = False

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] + data[j] == value:
                existence = True
                return existence

    return existence


def first_part(data, steps_back):

    for i in range(len(data)-steps_back):
        data_piece = data[i:i+steps_back]
        sum_value = data[i+steps_back]
        flag_existence = sum_exists(data_piece, sum_value)
        if flag_existence is False:
            return sum_value

    return None


def second_part(data):

    return


def day_9_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    input_data = open(path_to_input, 'r').readlines()
    input_data = [int(input_data[i].rstrip()) for i in range(len(input_data))]

    steps_back = 25
    answer_1 = first_part(input_data, steps_back)
    answer_2 = second_part(input_data)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_9_solution(input_folder_name, input_file_name)