from sys import argv
from os import chdir


def first_part(data):
    accumulator_value = 0
    already_executed = [False]*len(data)
    next_command_index = 0

    while already_executed[next_command_index] is False:
        command = data[next_command_index].split(' ')[0]
        value = int(data[next_command_index].split(' ')[1])
        already_executed[next_command_index] = True
        if command == 'nop':
            next_command_index += 1
        elif command == 'acc':
            next_command_index += 1
            accumulator_value += value
        elif command == 'jmp':
            next_command_index += value

    return accumulator_value


def second_part(data):
    accumulator_value = 0

    return accumulator_value


def day_8_solution(folder_name, file_name):

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
    day_8_solution(input_folder_name, input_file_name)