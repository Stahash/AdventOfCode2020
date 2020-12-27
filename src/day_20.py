from sys import argv
from os import chdir
from numpy import zeros, array_equal


def read_input_file(path_to_file):

    input_data = open(path_to_file, 'r').readlines()
    input_data = [line.strip() for line in input_data]

    tiles = dict()
    tile_number = 0

    for line in input_data:
        if line.startswith('Tile'):
            tile_number = int(line[:-1].split(' ')[1])
            new_tile = list()
        elif line.startswith('#') or line.startswith('.'):
            new_tile.append(line)
        elif line == '':
            tiles[tile_number] = new_tile

    tiles[tile_number] = new_tile

    rows_number = len(tiles[tile_number])
    columns_number = len(tiles[tile_number][0])

    for tile in tiles.keys():
        tile_as_array = zeros((rows_number, columns_number), dtype=str, order='C')

        for i in range(len(tiles[tile])):
            tile_as_array[i, :] = list(tiles[tile][i])

        tiles[tile] = tile_as_array

    return tiles


def first_part(all_tiles):

    corner_tiles = list()
    side_tiles = list()
    central_tiles = list()
    tiles_list = list(all_tiles.keys())

    for i in range(len(tiles_list)):
        print('Check tile {0} matches'.format(tiles_list[i]))
        tile_i = all_tiles[tiles_list[i]]
        tile_i_borders = (tile_i[0, :], tile_i[:, -1], tile_i[-1, :], tile_i[:, 0])
        tile_i_borders_match = 0

        for j in range(len(tiles_list)):

            if i != j:
                tile_j = all_tiles[tiles_list[j]]
                tile_j_borders = (tile_j[0, :], tile_j[:, -1], tile_j[-1, :], tile_j[:, 0])

                for n in range(4):
                    for k in range(4):
                        if array_equal(tile_i_borders[n], tile_j_borders[k]) or \
                                array_equal(tile_i_borders[n], tile_j_borders[k][::-1]):

                            tile_i_borders_match += 1
                            print('    Matches with tile {0}'.format(tiles_list[j]))

        if tile_i_borders_match == 2:
            corner_tiles.append(tiles_list[i])
        elif tile_i_borders_match == 3:
            side_tiles.append(tiles_list[i])
        elif tile_i_borders_match == 4:
            central_tiles.append(tiles_list[i])

    answer = corner_tiles[0] * corner_tiles[1] * corner_tiles[2] * corner_tiles[3]
    return answer


def second_part(all_tiles):

    return None


def day_20_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name
    tiles = read_input_file(path_to_input)
    answer_1 = first_part(tiles)
    print('Your puzzle answer for first part is {0}'.format(answer_1))

    answer_2 = second_part(tiles)
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_20_solution(input_folder_name, input_file_name)