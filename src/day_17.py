from sys import argv
from os import chdir
from numpy import zeros, count_nonzero


def read_input_file(path_to_file):

    input_data = open(path_to_file, 'r').readlines()
    input_data = [line.strip() for line in input_data]

    return input_data


def change_the_cube(cube):
    modified_cube = zeros(cube.shape, dtype=str, order='C')
    modified_cube.fill('.')

    cube_size = cube.shape[0]
    number_layers = cube.shape[2]

    for i in range(1, cube_size-1):
        for j in range(1, cube_size-1):
            for k in range(1, number_layers-1):

                little_cube = zeros((3, 3, 3), dtype=str, order='C')
                little_cube.fill('.')
                little_cube = cube[i-1:i+2, j-1:j+2, k-1:k+2]
                active_neighbours = count_nonzero(little_cube == '#')
                
                # limits increased by 1, because little cube is copy of the cube part and it's center can be '#'
                if cube[i, j, k] == '#' and 3 <= active_neighbours <= 4:
                    modified_cube[i, j, k] = '#'

                if cube[i, j, k] == '.' and active_neighbours == 3:
                    modified_cube[i, j, k] = '#'

    return modified_cube


def first_part(data, cycles):

    cube_size = len(data[0]) + 4
    number_layers = 5
    cube = zeros((cube_size, cube_size, number_layers), dtype=str, order='C')
    cube.fill('.')

    # initialize the cube
    for line_i in range(2, cube_size-2):
        cube[line_i, 2:cube_size-2, 2] = list(data[line_i-2])
    active_cubes = count_nonzero(cube == '#')

    for cycle_i in range(cycles):

        new_cube = change_the_cube(cube)

        active_cubes = count_nonzero(new_cube == '#')
        print('After {0} cycle {1} cubes are in active state'.format(cycle_i+1, active_cubes))

        cube_size += 4
        number_layers += 4

        cube = zeros((cube_size, cube_size, number_layers), dtype=str, order='C')
        cube.fill('.')
        cube[2:cube_size-2, 2:cube_size-2, 2:number_layers-2] = new_cube

    return active_cubes


def second_part(data):


    return None


def day_17_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    input_data = read_input_file(path_to_input)

    cycles_number = 6
    answer_1 = first_part(input_data, cycles_number)
    answer_2 = second_part(input_data)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_17_solution(input_folder_name, input_file_name)