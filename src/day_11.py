from sys import argv
from os import chdir
from numpy import zeros, array_equal, count_nonzero, diagonal


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


def count_occupied(list_coordinates, all_data):

    number_occupied = 0
    for coordinate_pair in list_coordinates:
        if all_data[coordinate_pair[0], coordinate_pair[1]] == '#':
            number_occupied += 1

    return number_occupied


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
                occupied_seats = count_occupied(existing_neighbours, data)
                if occupied_seats >= 4:
                    changed_data[row, column] = 'L'
                else:
                    changed_data[row, column] = '#'

            elif data[row, column] == 'L':
                occupied_seats = count_occupied(existing_neighbours, data)
                if occupied_seats == 0:
                    changed_data[row, column] = '#'
                else:
                    changed_data[row, column] = 'L'

    return changed_data


def neighbours_exist_new(current_row, current_column, row_limit, column_limit):

    directions_to_look = []

    if (current_row - 1) >= 0:  # upper
        directions_to_look.append((-1, 0))

    if ((current_row - 1) >= 0) and (current_column - 1 >= 0):  # upper left
        directions_to_look.append((-1, -1))

    if (current_column - 1) >= 0:  # left
        directions_to_look.append((0, -1))

    if ((current_row + 1) <= row_limit - 1) and ((current_column - 1) >= 0):  # down left
        directions_to_look.append((1, -1))

    if (current_row + 1) <= row_limit - 1:  # down
        directions_to_look.append((1, 0))

    if ((current_row + 1) <= row_limit - 1) and ((current_column + 1) <= column_limit - 1):  # down right
        directions_to_look.append((1, 1))

    if (current_column + 1) <= column_limit - 1:  # right
        directions_to_look.append((0, 1))

    if ((current_row - 1) >= 0) and (current_column + 1 <= column_limit - 1):  # upper right
        directions_to_look.append((-1, 1))

    return directions_to_look


def go_along_direction(row, column, step_i, step_j, all_data):

    seat_occupied = False
    row_limit = all_data.shape[0]
    column_limit = all_data.shape[1]

    new_x = row + step_i
    new_y = column + step_j

    while (0 <= new_x <= row_limit - 1) and (0 <= new_y <= column_limit - 1):
        if all_data[new_x, new_y] == '.':
            new_x += step_i
            new_y += step_j
        else:
            if all_data[new_x, new_y] == '#':
                seat_occupied = True
            else:
                seat_occupied = False
            return seat_occupied

    return seat_occupied


def count_occupied_new(list_coordinates, all_data, current_row, current_column):

    number_occupied = 0
    if (-1, 0) in list_coordinates:  # look to upper direction
        is_occupied = go_along_direction(current_row, current_column, -1, 0, all_data)
        if is_occupied is True:
            number_occupied += 1

    if (-1, -1) in list_coordinates:  # look to upper left
        is_occupied = go_along_direction(current_row, current_column, -1, -1, all_data)
        if is_occupied is True:
            number_occupied += 1

    if (0, -1) in list_coordinates:  # look to left direction
        is_occupied = go_along_direction(current_row, current_column, 0, -1, all_data)
        if is_occupied is True:
            number_occupied += 1

    if (1, -1) in list_coordinates:  # look to down left
        is_occupied = go_along_direction(current_row, current_column, 1, -1, all_data)
        if is_occupied is True:
            number_occupied += 1

    if (1, 0) in list_coordinates: # look down direction
        is_occupied = go_along_direction(current_row, current_column, 1, 0, all_data)
        if is_occupied is True:
            number_occupied += 1

    if (1, 1) in list_coordinates:  # look down right direction
        is_occupied = go_along_direction(current_row, current_column, 1, 1, all_data)
        if is_occupied is True:
            number_occupied += 1

    if (0, 1) in list_coordinates: # look right direction
        is_occupied = go_along_direction(current_row, current_column, 0, 1, all_data)
        if is_occupied is True:
            number_occupied += 1

    if (-1, 1) in list_coordinates: # look upper right direction
        is_occupied = go_along_direction(current_row, current_column, -1, 1, all_data)
        if is_occupied is True:
            number_occupied += 1

    return number_occupied


def apply_new_rules(data):
    # People don't just care about adjacent seats -
    # they care about the first seat they can see in each of those eight directions!

    # Also, people seem to be more tolerant than you expected:
    # it now takes five or more visible occupied seats for an occupied seat to become empty
    # (rather than four or more from the previous rules).

    changed_data = zeros(data.shape, dtype=str, order='C')

    for row in range(data.shape[0]):
        for column in range(data.shape[1]):

            existing_neighbours = neighbours_exist_new(row, column, data.shape[0], data.shape[1])

            if data[row, column] == '.':
                changed_data[row, column] = '.'

            elif data[row, column] == '#':
                occupied_seats = count_occupied_new(existing_neighbours, data, row, column)
                if occupied_seats >=5:
                    changed_data[row, column] = 'L'
                else:
                    changed_data[row, column] = '#'

            elif data[row, column] == 'L':
                occupied_seats = count_occupied_new(existing_neighbours, data, row, column)
                if occupied_seats == 0:
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

    data_before_round = data
    data_after_round = zeros(data.shape, dtype=str, order='C')
    finished = False

    while finished is False:
        data_after_round = apply_new_rules(data_before_round)
        if array_equal(data_after_round, data_before_round) is True:
            finished = True
        else:
            data_before_round = data_after_round

    occupied_seats = count_nonzero(data_after_round == '#')

    return occupied_seats


def day_11_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    input_data = open(path_to_input, 'r').readlines()
    input_data = [input_data[i].rstrip() for i in range(len(input_data))]
    input_matrix = create_input_matrix(input_data)

    answer_1 = first_part(input_matrix)
    answer_2 = second_part(input_matrix)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_11_solution(input_folder_name, input_file_name)