from sys import argv
from os import chdir


def read_input_file(path_to_file):

    input_data = open(path_to_file, 'r').read().rstrip().split(',')
    input_data = [int(input_data[i]) for i in range(len(input_data))]

    return input_data


def first_part(data, turn_limit):

    turns_number = len(data)
    speaking_numbers = data.copy()
    number_and_occurences = dict()

    for i in range(len(speaking_numbers)):
        number_and_occurences[speaking_numbers[i]] = [i + 1]

    while turns_number < turn_limit:

        turns_number += 1

        last_number = speaking_numbers[-1]
        occurences = len(number_and_occurences[last_number])

        if occurences == 1:
            speaking_numbers.append(0)
            number_and_occurences[0] = number_and_occurences.get(0, list())
            number_and_occurences[0].append(turns_number)
            continue
        else:
            last_occurence = number_and_occurences[last_number][-1]
            previous_occurence = number_and_occurences[last_number][-2]
            number_and_occurences[last_number] = [previous_occurence, last_occurence]

            new_number = last_occurence - previous_occurence
            speaking_numbers.append(new_number)

            number_and_occurences[new_number] = number_and_occurences.get(new_number, list())
            number_and_occurences[new_number].append(turns_number)

        print('Turn {0}. Spoken number {1}'.format(turns_number, speaking_numbers[-1]))

    answer = speaking_numbers[-1]

    return answer


def day_15_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    input_content = read_input_file(path_to_input)

    max_turn = 2020
    answer_1 = first_part(input_content, max_turn)

    max_turn = 30000000
    answer_2 = first_part(input_content, max_turn)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_15_solution(input_folder_name, input_file_name)