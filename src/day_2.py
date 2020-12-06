from os import chdir
from sys import argv


def first_part(data):
    number_correct_pass = 0
    for pass_index in range(len(data)):
        current_line = data[pass_index].split()
        min_times = int(current_line[0].split('-')[0])
        max_times = int(current_line[0].split('-')[1])
        main_letter = current_line[1][0]
        password = current_line[2]

        occurence = password.count(main_letter)
        if (occurence >= min_times) and (occurence <= max_times):
            number_correct_pass += 1

    return number_correct_pass


def second_part(data):
    number_correct_pass = 0
    number_incorrect_pass = 0

    for pass_index in range(len(data)):
        current_line = data[pass_index].split()
        min_position_index = int(current_line[0].split('-')[0])
        max_position_index = int(current_line[0].split('-')[1])
        main_letter = current_line[1][0]
        password = current_line[2]

        if max_position_index <= len(password):
            if (password[min_position_index - 1] == main_letter) and (password[max_position_index - 1] == main_letter):
                number_incorrect_pass += 1
            elif (password[min_position_index - 1] != main_letter) and (password[max_position_index - 1] != main_letter):
                number_incorrect_pass += 1
            else:
                number_correct_pass += 1

    return number_correct_pass


def day_2_solution(folder_name, file_name):

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
    day_2_solution(input_folder_name, input_file_name)
