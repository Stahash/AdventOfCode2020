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


def get_buses_sequence(path_to_file):
    input_data = open(path_to_file, 'r').readlines()
    input_data = [input_data[i].rstrip() for i in range(len(input_data))]

    all_buses = input_data[1].split(',')
    all_available_buses = [int(all_buses[i]) for i in range(len(all_buses)) if all_buses[i] != 'x']

    bus_time = [all_buses.index(str(bus_id)) for bus_id in all_available_buses]

    return all_available_buses, bus_time


def second_part(buses_id, buses_timetable):

    timestep_found = False
    n = floor(100000000000000 / buses_id[0])
    answer = 0

    while timestep_found is False:
        possible_timestep = buses_id[0]*n
        print('Time step {0}'.format(possible_timestep))

        check_next_bus = False
        for bus in range(1, len(buses_id)):
            if (possible_timestep + buses_timetable[bus]) % buses_id[bus] == 0:
                check_next_bus = True
            else:
                check_next_bus = False
                break

        if check_next_bus is True:
            timestep_found = True
            answer = possible_timestep
        else:
            n += 1

    return answer


def day_13_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    timestamp, buses_IDs = read_input_file(path_to_input)
    answer_1 = first_part(timestamp, buses_IDs)

    buses, delta_t = get_buses_sequence(path_to_input)
    answer_2 = second_part(buses, delta_t)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_13_solution(input_folder_name, input_file_name)