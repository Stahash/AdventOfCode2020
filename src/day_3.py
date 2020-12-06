from sys import argv
from os import chdir
from math import ceil


def create_new_map(initial_map, to_right, to_down):
    rows_number = len(initial_map)
    initial_line_length = len(initial_map[0])
    multiplier = ceil((to_right * to_down * rows_number) / initial_line_length)
    new_map = [initial_map[i]*multiplier for i in range(rows_number)]

    return new_map


def count_trees(current_map, to_right, to_down):
    rows_number = len(current_map)
    free_space = 0
    trees = 0
    current_x = 0

    indices = list(range(0, rows_number, to_down))

    for line_i in indices:
        current_line = current_map[line_i]
        if current_line[current_x] == '.':
            free_space += 1
        elif current_line[current_x] == '#':
            trees += 1
        current_x += to_right

    return trees


def first_part(data):
    steps_right = 3
    steps_down = 1
    new_data = create_new_map(data, steps_right, steps_down)
    trees_number = count_trees(new_data, steps_right, steps_down)

    return trees_number


def second_part(data):
    answer = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    for slope in slopes:
        new_data = create_new_map(data, slope[0], slope[1])
        number_trees = count_trees(new_data, slope[0], slope[1])
        answer *= number_trees

    return answer


def day_3_solution(folder_name, file_name):

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
    day_3_solution(input_folder_name, input_file_name)