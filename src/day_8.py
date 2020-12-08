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


def is_change_helped(data):
    already_executed = [False] * len(data)
    next_command_index = 0
    output_value = 0

    change_helped = False
    while already_executed[next_command_index] is False:
        command = data[next_command_index].split(' ')[0]
        value = int(data[next_command_index].split(' ')[1])
        already_executed[next_command_index] = True
        if command == 'nop':
            next_command_index += 1
        elif command == 'acc':
            next_command_index += 1
            output_value += value
        elif command == 'jmp':
            next_command_index += value

        if (next_command_index < 0) or (next_command_index >= len(data)):
            change_helped = True
            break

    return change_helped, output_value


def change_command(command_index, to_change, data):

    changed_data = data.copy()
    changed_data[command_index] = to_change + ' ' + changed_data[command_index].split(' ')[1]
    flag_change_helped, acc_value = is_change_helped(changed_data)

    return flag_change_helped, acc_value


def second_part(data):
    accumulator_value = 0
    nop_indexes = [i for i in range(len(data)) if data[i].split(' ')[0] == 'nop']
    jmp_indexes = [i for i in range(len(data)) if data[i].split(' ')[0] == 'jmp']

    for index in nop_indexes:
        no_infinite_loop, accumulator_value = change_command(index, 'jmp', data)
        if no_infinite_loop is True:
            return accumulator_value

    for index in jmp_indexes:
        no_infinite_loop, accumulator_value = change_command(index, 'nop', data)
        if no_infinite_loop is True:
            return accumulator_value

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