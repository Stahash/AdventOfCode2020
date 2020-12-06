from os import chdir
from sys import argv


def first_part(data):
    minimum_value = min(data)
    cutted_data = [x for x in data if x < (2020 - minimum_value)]
    print('- Solving first part')
    for i in range(len(cutted_data)):
        for j in range(i, len(cutted_data)):
            if cutted_data[i] + cutted_data[j] == 2020:
                print('Number 1 is {0} at {1} position in the list'.format(cutted_data[i], j))
                print('Number 2 is {0} at {1} position in the list'.format(cutted_data[j], j))
                return cutted_data[i] * cutted_data[j]


def second_part(data):
    minimum_value = min(data)
    cutted_data = [x for x in data if x < (2020 - minimum_value)]
    sorted_cutted_data = sorted(set(cutted_data))
    more_cutted_data = [x for x in cutted_data if x < (2020 - sorted_cutted_data[0] - sorted_cutted_data[1])]

    print('- Solving second part')
    for i in range(len(more_cutted_data)):
        rest = 2020 - more_cutted_data[i]
        for j in range(i, len(more_cutted_data)):
            for k in range(j, len(more_cutted_data)):
                if more_cutted_data[j] + more_cutted_data[k] == rest:
                    print('Number 1 is {0} at {1} position in the list'.format(more_cutted_data[i], i))
                    print('Number 2 is {0} at {1} position in the list'.format(more_cutted_data[j], j))
                    print('Number 3 is {0} at {1} position in the list'.format(more_cutted_data[k], k))
                    return more_cutted_data[i] * more_cutted_data[j] * more_cutted_data[k]


def day_1_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    input_data = open(path_to_input, 'r').readlines()
    input_data = [int(input_data[i].rstrip()) for i in range(len(input_data))]

    answer_1 = first_part(input_data)
    answer_2 = second_part(input_data)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_1_solution(input_folder_name, input_file_name)




