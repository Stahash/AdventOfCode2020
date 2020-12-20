from sys import argv
from os import chdir
from numpy import binary_repr


def read_input_file(path_to_file):

    input_data = open(path_to_file, 'r').readlines()
    input_data = [input_data[i].rstrip() for i in range(len(input_data))]

    return input_data


def use_mask(number_initial, mask):

    new_number_str = ''
    for i in range(len(mask)):

        if mask[i] == 'X':
            new_number_str += number_initial[i]
        elif mask[i] == '1':
            new_number_str += '1'
        elif mask[i] == '0':
            new_number_str += '0'

    decimal_number = int(new_number_str, 2)

    return decimal_number


def first_part(masks_mems):

    current_mask = 'X'*36
    memory_numbers = dict()

    for line in masks_mems:

        if line.startswith('mask'):
            current_mask = line.split('=')[1].strip()

        elif line.startswith('mem'):
            mem_address = int(line.split('=')[0].strip().split('[')[1].split(']')[0])
            to_write = int(line.split('=')[1].strip())
            number_in_binary = binary_repr(to_write, width=36)

            put_to_mem = use_mask(number_in_binary, current_mask)
            memory_numbers[mem_address] = memory_numbers.get(mem_address, 0)
            memory_numbers[mem_address] = put_to_mem

    answer = sum(memory_numbers.values())

    return answer


def second_part(masks_mems):

    return None


def day_14_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    input_content = read_input_file(path_to_input)
    answer_1 = first_part(input_content)
    answer_2 = second_part(input_content)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_14_solution(input_folder_name, input_file_name)