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


def move_waypoint_without_rotation(current_direction, delta, prev_x, prev_y):

    new_x = None
    new_y = None

    if current_direction == 'N':
        new_x = prev_x
        new_y = prev_y + delta
    elif current_direction == 'S':
        new_x = prev_x
        new_y = prev_y - delta
    elif current_direction == 'E':
        new_x = prev_x + delta
        new_y = prev_y
    elif current_direction == 'W':
        new_x = prev_x - delta
        new_y = prev_y

    return new_x, new_y


def move_ship(delta,
              current_waypoint_x, current_waypoint_y,
              current_ship_x, current_ship_y):

    new_ship_x = current_ship_x + delta*current_waypoint_x
    new_ship_y = current_ship_y + delta*current_waypoint_y

    return new_ship_x, new_ship_y


def change_compass_course(current_direction, delta, prev_waypoint_x, prev_waypoint_y):

    new_waypoint_x = None
    new_waypoint_y = None

    new_angle = delta % 360

    if new_angle == 0 and current_direction in ['L', 'R']:
        new_waypoint_x = prev_waypoint_x
        new_waypoint_y = prev_waypoint_y

    if new_angle == 180 and current_direction in ['L', 'R']:
        new_waypoint_x = -prev_waypoint_x
        new_waypoint_y = -prev_waypoint_y

    if new_angle == 90 and current_direction == 'L':
        new_waypoint_x = -prev_waypoint_y
        new_waypoint_y = prev_waypoint_x

    if new_angle == 90 and current_direction == 'R':
        new_waypoint_x = prev_waypoint_y
        new_waypoint_y = -prev_waypoint_x

    if new_angle == 270 and current_direction == 'L':
        new_waypoint_x = prev_waypoint_y
        new_waypoint_y = -prev_waypoint_x

    if new_angle == 270 and current_direction == 'R':
        new_waypoint_x = -prev_waypoint_y
        new_waypoint_y = prev_waypoint_x

    return new_waypoint_x, new_waypoint_y


def second_part(data):

    ship_x = 0
    ship_y = 0

    waypoint_x = 10
    waypoint_y = 1

    for command in data:
        direction = command[0]
        steps = int(command[1:])

        if direction in ['N', 'S', 'W', 'E']:
            waypoint_x, waypoint_y = \
                move_waypoint_without_rotation(direction, steps, waypoint_x, waypoint_y)

        elif direction == 'F':
            ship_x, ship_y = move_ship(steps, waypoint_x, waypoint_y, ship_x, ship_y)

        elif direction in ['L', 'R']:
            waypoint_x, waypoint_y = change_compass_course(direction, steps, waypoint_x, waypoint_y)

    return abs(ship_x) + abs(ship_y)


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