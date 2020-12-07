from sys import argv
from os import chdir
from re import findall


def find_parents(list_bags, data):

    list_parents = list()

    for bag_rule in data:

        for bag in list_bags:
            contain_bags = bag_rule.split('contain')[1]
            if len(findall(bag, contain_bags)) != 0:
                list_parents.append(bag_rule.split('contain')[0].strip().split('bags')[0].strip())

    list_parents = list(set(list_parents))

    return list_parents


def find_childrens(list_bags, data):

    list_childrens = list()

    for bag_rule in data:

        for bag in list_bags:
            contain_bags = bag_rule.split('contain')[0]
            if len(findall(bag, contain_bags)) != 0:
                list_childrens.append(bag_rule.split('contain')[1].strip().split(','))

    list_parents = list(set(list_childrens))

    return list_parents


def first_part(data):

    your_bag = ['shiny gold']
    list_bags = find_parents(your_bag, data)
    possible_parents = list_bags

    while len(list_bags) != 0:
        list_bags = find_parents(list_bags, data)
        possible_parents += list_bags

    all_parents_number = len(set(possible_parents))

    return all_parents_number


def second_part(data):

    your_bag = ['shiny gold']
    list_bags = find_childrens(your_bag, data)
    possible_parents = list_bags


def day_7_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    input_data = open(path_to_input, 'r').readlines()
    input_data = [input_data[i].rstrip() for i in range(len(input_data))]

    answer_1 = first_part(input_data)
   # answer_2 = second_part(input_data)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
  #  print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_7_solution(input_folder_name, input_file_name)