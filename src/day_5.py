from sys import argv
from os import chdir
from math import floor, ceil


def find_row(row_code, all_rows):
    zone_to_look = (0, all_rows-1)
    for letter in row_code:
        if letter == "F":
            last = floor(zone_to_look[0]+((zone_to_look[1]-zone_to_look[0])/2))
            zone_to_look = (zone_to_look[0], last)
        elif letter == "B":
            first = ceil(zone_to_look[0]+((zone_to_look[1]-zone_to_look[0])/2))
            zone_to_look = (first, zone_to_look[1])
        else:
            print("Only F and B letters are allowed in the part for row. Letter {0} is incorrect".format(letter))

    your_row = zone_to_look[0]
    return your_row


def find_column(column_code, all_columns):
    zone_to_look = (0, all_columns - 1)
    for letter in column_code:
        if letter == "L":
            last = floor(zone_to_look[0] + ((zone_to_look[1] - zone_to_look[0]) / 2))
            zone_to_look = (zone_to_look[0], last)
        elif letter == "R":
            first = ceil(zone_to_look[0] + ((zone_to_look[1] - zone_to_look[0]) / 2))
            zone_to_look = (first, zone_to_look[1])
        else:
            print("Only L and R letters are allowed in the part for row. Letter {0} is incorrect".format(letter))

    your_column = zone_to_look[0]
    return your_column


def find_id(your_row, your_column):
    your_id = your_row*8 + your_column
    return your_id


def first_part(data):

    rows_number = 128
    columns_number = 8
    all_id = list()

    for boarding_pass in data:
        row = find_row(boarding_pass[0:7], rows_number)
        column = find_column(boarding_pass[-3:], columns_number)
        id = find_id(row, column)
        all_id.append(id)

    return max(all_id), all_id


def second_part(data):
    set_ids = set(data)
    set_all_possible_ids = set(range(0, max(data)))

    difference = set_all_possible_ids.difference(set_ids)

    for id in difference:
        if ((id+1) in set_ids) and ((id-1) in set_ids):
            return id


def day_5_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    input_data = open(path_to_input, 'r').readlines()
    input_data = [input_data[i].rstrip() for i in range(len(input_data))]

    answer_1, all_id = first_part(input_data)
    answer_2 = second_part(all_id)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_5_solution(input_folder_name, input_file_name)
