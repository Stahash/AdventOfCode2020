from sys import argv
from os import chdir


def read_input_file(path_to_file):

    input_data = open(path_to_file, 'r').read().rstrip().split(',')
    input_data = [int(input_data[i]) for i in range(len(input_data))]

    return input_data


def first_part(data):

    turns_number = len(data)
    speaking_numbers = data.copy()

    while turns_number < 2020:

        turns_number += 1

        last_number = speaking_numbers[-1]
        occurences = speaking_numbers.count(last_number)

        if occurences == 1:
            speaking_numbers.append(0)
            continue
        else:
            last_occurence = len(speaking_numbers)
            previous_occurence = [i+1 for i, x in enumerate(speaking_numbers)
                                  if x == last_number and i < len(speaking_numbers) - 1]

            speaking_numbers.append(last_occurence-previous_occurence[-1])

    answer = speaking_numbers[-1]

    return answer


def second_part(data):


    return None


def day_15_solution(folder_name, file_name):

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
    day_15_solution(input_folder_name, input_file_name)