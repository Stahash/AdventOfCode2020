from sys import argv
from os import chdir
from time import time


def first_part(data):

    one_jolt_differences = 0
    two_jolt_differences = 0
    three_jolt_differences = 0

    min_value = min(data)

    if min_value not in [1, 2, 3]:
        print('There is no available adapter to start')
        return None

    if min_value == 1:
        one_jolt_differences += 1
    elif min_value == 2:
        two_jolt_differences += 1
    elif min_value == 3:
        three_jolt_differences += 1

    current_index = data.index(min_value)

    while current_index <= len(data)-1:
        current_value = data[current_index]
        if (current_value + 1) in data:
            one_jolt_differences += 1
            current_index = data.index(current_value + 1)
            continue
        elif (current_value + 2) in data:
            two_jolt_differences += 1
            current_index = data.index(current_value + 2)
            continue
        elif (current_value + 3) in data:
            three_jolt_differences += 1
            current_index = data.index(current_value + 3)
            continue
        else:
            print('Stop searching: there is no more available adapter in the list')
            break

    three_jolt_differences += 1

    return one_jolt_differences * three_jolt_differences


def find_children(parents, data, last_node):

    children = dict()

    for node, node_freq in parents.items():
        if (node + 1) in data:
            children[node + 1] = children.get(node+1, 0) + node_freq
        if (node + 2) in data:
            children[node+2] = children.get(node+2, 0) + node_freq
        if (node + 3) in data:
            children[node+3] = children.get(node+3, 0) + node_freq

    finished_paths_number = children.get(last_node, 0)

    return children, finished_paths_number


def second_part(data):
    start_time = time()

    starting_node = 0
    sorted_data = sorted(data)
    final_node = max(data) + 3
    sorted_data.append(final_node)
    children = {starting_node: 1}

    number_paths = 0
    while children:
        children, finished_paths = find_children(children, sorted_data, final_node)
        number_paths += finished_paths

    execution_time = time() - start_time
    print('Took {0} seconds'.format(execution_time))

    return number_paths


def day_10_solution(folder_name, file_name):

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
    day_10_solution(input_folder_name, input_file_name)