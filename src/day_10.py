from sys import argv
from os import chdir


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


def find_children(previous_children, data):

    next_children = list()

    for child in previous_children:

        if (child + 1) in data:
            next_children.append(child + 1)

        if (child + 2) in data:
            next_children.append(child + 2)

        if (child + 3) in data:
            next_children.append(child + 3)

    return next_children


def second_part(data):

    starting_node = 0
    sorted_data = sorted(data)
    sorted_data.append(max(data)+3)
    list_children = list()
    list_children.append(starting_node)

    max_number_children = 0

    while list_children:
        list_children = find_children(list_children, sorted_data)
        if len(list_children) > max_number_children:
            max_number_children = len(list_children)

    return max_number_children


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