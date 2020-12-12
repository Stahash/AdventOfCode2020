from sys import argv
from os import chdir


def change_angle(current_angle, new_direction, degrees):

    new_angle = None
    if new_direction == 'L':
        new_angle = current_angle + degrees
    elif new_direction == 'R':
        new_angle = current_angle - degrees

    new_angle = new_angle % 360

    return new_angle


def first_part(data):

    x = 0
    y = 0
    angle = 0

    for command in data:
        direction = command[0]
        steps = int(command[1:])

        if direction == 'N':
            y = y + steps
        elif direction == 'S':
            y = y - steps
        elif direction == 'E':
            x = x + steps
        elif direction == 'W':
            x = x - steps

        if direction in ['L', 'R']:
            angle = change_angle(angle, direction, steps)

        if direction == 'F':
            if angle == 0:
                x = x + steps
            elif angle in [270, -90]:
                y = y - steps
            elif angle in [-180, 180]:
                x = x - steps
            elif angle in [-270, 90]:
                y = y + steps

    return abs(x) + abs(y)


def second_part(data):



    return None


def day_12_solution(folder_name, file_name):

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
    day_12_solution(input_folder_name, input_file_name)