from sys import argv
from os import chdir
from numpy import zeros, array_equal, count_nonzero


def create_input_matrix(data):
    num_rows = len(data)
    num_columns = len(data[0])
    initial_data = zeros((num_rows, num_columns), dtype=str, order='C')
    for row in range(num_rows):
        initial_data[row, :] = list(data[row])
    return initial_data


def neighbours_exist(current_row, current_column, row_limit, column_limit):

    coordinates_to_look = []

    if (current_row - 1) >= 0:  # upper
        coordinates_to_look.append((current_row-1, current_column))

    if ((current_row - 1) >= 0) and (current_column - 1 >= 0):  # upper left
        coordinates_to_look.append((current_row - 1, current_column - 1))

    if (current_column - 1) >= 0:  # left
        coordinates_to_look.append((current_row, current_column - 1))

    if ((current_row + 1) <= row_limit - 1) and ((current_column - 1) >= 0):  # down left
        coordinates_to_look.append((current_row + 1, current_column - 1))

    if (current_row + 1) <= row_limit - 1:  # down
        coordinates_to_look.append((current_row + 1, current_column))

    if ((current_row + 1) <= row_limit - 1) and ((current_column + 1) <= column_limit - 1):  # down right
        coordinates_to_look.append((current_row + 1, current_column + 1))

    if (current_column + 1) <= column_limit - 1:  # right
        coordinates_to_look.append((current_row, current_column + 1))

    if ((current_row - 1) >= 0) and (current_column + 1 <= column_limit - 1):  # upper right
        coordinates_to_look.append((current_row - 1, current_column + 1))

    return coordinates_to_look


def check_occupied_adjacent(list_coordinates, all_data):
    change_to_empty_flag = False

    count_occupied = 0
    for coordinate_pair in list_coordinates:
        if all_data[coordinate_pair[0], coordinate_pair[1]] == '#':
            count_occupied += 1

    if count_occupied >= 4:
        change_to_empty_flag = True

    return change_to_empty_flag


def check_empty_adjacent(list_coordinates, all_data):

    change_to_occupied_flag = False

    count_occupied = 0
    for coordinate_pair in list_coordinates:
        if all_data[coordinate_pair[0], coordinate_pair[1]] == '#':
            count_occupied += 1

    if count_occupied == 0:
        change_to_occupied_flag = True

    return change_to_occupied_flag


def apply_rules(data):
    # If a seat is empty(L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    # Otherwise, the seat 's state does not change.
    # Floor(.) never changes; seats don't move, and nobody sits on the floor.

    changed_data = zeros(data.shape, dtype=str, order='C')

    for row in range(data.shape[0]):
        for column in range(data.shape[1]):

            existing_neighbours = neighbours_exist(row, column, data.shape[0], data.shape[1])

            if data[row, column] == '.':
                changed_data[row, column] = '.'

            elif data[row, column] == '#':
                change_to_empty = check_occupied_adjacent(existing_neighbours, data)
                if change_to_empty is True:
                    changed_data[row, column] = 'L'
                else:
                    changed_data[row, column] = '#'
            elif data[row, column] == 'L':
                change_to_occupied = check_empty_adjacent(existing_neighbours, data)
                if change_to_occupied is True:
                    changed_data[row, column] = '#'
                else:
                    changed_data[row, column] = 'L'

    return changed_data


def first_part(data):

    data_before_round = data
    data_after_round = zeros(data.shape, dtype=str, order='C')
    finished = False

    while finished is False:
        data_after_round = apply_rules(data_before_round)
        if array_equal(data_after_round, data_before_round) is True:
            finished = True
        else:
            data_before_round = data_after_round

    occupied_seats = count_nonzero(data_after_round == '#')

    return occupied_seats


def second_part(data):


    return None


def day_11_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    input_data = open(path_to_input, 'r').readlines()
    input_data = [input_data[i].rstrip() for i in range(len(input_data))]
    input_matrix = create_input_matrix(input_data)

    answer_1 = first_part(input_matrix)
    answer_2 = second_part(input_data)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_11_solution(input_folder_name, input_file_name)