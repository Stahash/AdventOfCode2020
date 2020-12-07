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

    childrens = dict()
    number_childrens = 0

    for bag_rule in data:
        bag_rule = bag_rule[:-1]

        for bag in list_bags.keys():
            contain_bags = bag_rule.split('contain')[0]
            if len(findall(bag, contain_bags)) != 0:

                if bag_rule.split('contain')[1].strip() != 'no other bags':
                    bag_contain = bag_rule.split('contain')[1].strip().split(',')
                    bag_contain = [bag_contain[i].strip() for i in range(len(bag_contain))]
                    number_bugs = [int(bag_contain[i].split()[0]) for i in range(len(bag_contain))]
                    bugs_names = [' '.join(bag_contain[i].split()[1:3]) for i in range(len(bag_contain))]

                    for bag_name, number in zip(bugs_names, number_bugs):
                        if bag_name in childrens:
                            childrens[bag_name] += number * list_bags[bag]
                        else:
                            childrens[bag_name] = number * list_bags[bag]

                    number_childrens += sum(number_bugs) * list_bags[bag]

    return childrens, number_childrens


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

    total_bags_number = 0
    your_bag = {'shiny gold': 1}
    list_bags, number_bags = find_childrens(your_bag, data)
    total_bags_number += number_bags

    while len(list_bags) != 0:
        list_bags, number_bags = find_childrens(list_bags, data)
        total_bags_number += number_bags

    return total_bags_number


def day_7_solution(folder_name, file_name):

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
    day_7_solution(input_folder_name, input_file_name)