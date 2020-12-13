from sys import argv
from os import chdir
from math import floor


def read_input_file(path_to_file):

    input_data = open(path_to_file, 'r').readlines()
    input_data = [input_data[i].rstrip() for i in range(len(input_data))]

    earliest_time = int(input_data[0])
    all_available_buses = input_data[1].split(',')
    all_available_buses = [int(all_available_buses[i]) for i in range(len(all_available_buses))
                           if all_available_buses[i] != 'x']

    return earliest_time, sorted(all_available_buses)


def first_part(arrival_time, list_IDs):

    waiting_times = list()

    for bus_id in list_IDs:
        n = floor(arrival_time/bus_id) + 1
        nearest_time = bus_id * n
        waiting_times.append(nearest_time - arrival_time)

    minimum_waiting_time = min(waiting_times)
    correct_bus = list_IDs[waiting_times.index(minimum_waiting_time)]

    return minimum_waiting_time*correct_bus


def second_part(arrival_time, list_IDs):

    return None


def day_13_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    timestamp, buses_IDs = read_input_file(path_to_input)

    answer_1 = first_part(timestamp, buses_IDs)
    answer_2 = second_part(timestamp, buses_IDs)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_13_solution(input_folder_name, input_file_name)