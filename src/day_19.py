from sys import argv
from os import chdir
from itertools import product


def read_input_file(path_to_file):

    input_data = open(path_to_file, 'r').readlines()
    input_data = [line.strip() for line in input_data]

    rules = dict()
    messages_start_from = 0
    for line_i in range(len(input_data)):
        if ':' in input_data[line_i]:
            rule_index = input_data[line_i].split(':')[0]
            rule_text = input_data[line_i].split(':')[1].strip()
            rules[rule_index] = rule_text
        else:
            messages_start_from = line_i
            break

    messages = input_data[messages_start_from+1:]

    return rules, messages


def find_initials_ab_positions(rules_set):

    rule_a = next((key for key in rules_set if rules_set[key] == '"a"'), None)
    rule_b = next((key for key in rules_set if rules_set[key] == '"b"'), None)

    return rule_a, rule_b


def format_rules(rules_set, pos_a, pos_b):

    rules_set[pos_a] = 'a'
    rules_set[pos_b] = 'b'

    for rule in rules_set.keys():
        if '|' in rules_set[rule]:
            formated_rule = rules_set[rule].split('|')
            formated_rule = [sub_rule.strip() for sub_rule in formated_rule]
            rules_set[rule] = formated_rule
        else:
            formated_rule = rules_set[rule]
            rules_set[rule] = [formated_rule]

    return rules_set


def check_main_rule(main_rule):

    consists_of_letters = True
    for sub_rule in main_rule:
        elements = sub_rule.split(' ')
        if set(elements) not in [{'a', 'b'}, {'a'}, {'b'}]:
            consists_of_letters = False
            return consists_of_letters

    return consists_of_letters


def substitute_rules(rules_set, substitutes):

    for substitute in substitutes.keys():
        rule_substitute = substitutes[substitute]

        for rule in rules_set.keys():
            current_rule = rules_set[rule]
            updated_rule = list()

            for sub_rule in current_rule:
                elements = sub_rule.split(' ')
                if substitute in elements:
                    index = [i for i in range(len(elements)) if elements[i] == substitute]
                    variants = list(product(rule_substitute, repeat=len(index)))

                    for variant in variants:

                        for i in range(len(index)):
                            elements[index[i]] = variant[i]

                        modified_subrule = ' '.join(elements)
                        updated_rule.append(modified_subrule)

                else:
                    updated_rule.append(sub_rule)

            rules_set[rule] = updated_rule

    return rules_set


def delete_substitutes(rules_set, substitutes):

    for substitute in substitutes.keys():
        del rules_set[substitute]

    return rules_set


def find_substitutes(rules_set):

    substitutes = dict()

    for rule in rules_set.keys():
        current_rule = rules_set[rule]
        consists_of_letters = list()

        for sub_rule in current_rule:
            elements = sub_rule.split(' ')
            if set(elements) not in [{'a', 'b'}, {'a'}, {'b'}]:
                consists_of_letters.append(False)
            else:
                consists_of_letters.append(True)

        if False not in consists_of_letters:
            substitutes[rule] = rules_set[rule]

    return substitutes


def correct_messages_variants(main_rule):

    correct_messages = [''.join(sub_rule.split(' ')) for sub_rule in main_rule]
    return correct_messages


def check_messages_correctness(correct_messages_examples, all_messages):
    correct_messages_number = 0

    for message in all_messages:
        if message in correct_messages_examples:
            correct_messages_number += 1

    return correct_messages_number


def first_part(rules, messages):

    a_position, b_position = find_initials_ab_positions(rules)
    rules = format_rules(rules, a_position, b_position)
    main_rule_ready = check_main_rule(rules['0'])
    substitutes_list = {a_position: rules[a_position], b_position: rules[b_position]}

    while main_rule_ready is False:
        rules = delete_substitutes(rules, substitutes_list)
        rules = substitute_rules(rules, substitutes_list)
        substitutes_list = find_substitutes(rules)
        main_rule_ready = check_main_rule(rules['0'])

    correct_messages = correct_messages_variants(rules['0'])
    number_correct_messages = check_messages_correctness(correct_messages, messages)

    return number_correct_messages


def correct_rest_of_rules(rules_set):

    for rule in rules_set.keys():
        current_rule = rules_set[rule]

        if rule != '0':
            ab_subrules = list()
            recursive_subrules = list()
            for sub_rule in current_rule:
                elements = sub_rule.split(' ')
                if set(elements) in [{'a', 'b'}, {'a'}, {'b'}]:
                    ab_subrules.append(sub_rule)
                else:
                    recursive_subrules.append(sub_rule)

            updated_rule = list()
            for sub_rule_i in ab_subrules:
                updated_rule.append(sub_rule_i)

            for sub_rule_i in recursive_subrules:
                elements = sub_rule_i.split(' ')
                index = [i for i in range(len(elements)) if elements[i] == rule]
                variants = list(product(ab_subrules, repeat=len(index)))
                for variant in variants:
                    for i in range(len(index)):
                        elements[index[i]] = variant[i]

                    modified_subrule = ' '.join(elements)
                    updated_rule.append(modified_subrule)

            rules_set[rule] = updated_rule

    return rules_set


def find_correct_messages(possible_messages, all_messages):

    correct_messages = 0
    for message in possible_messages:
        current_message = ''.join(message.split(' '))
        if current_message in all_messages:
            correct_messages += 1

    return correct_messages


def second_part(rules, messages):

    print('Second part:')
    a_position, b_position = find_initials_ab_positions(rules)
    rules = format_rules(rules, a_position, b_position)
    substitutes_list = {a_position: rules[a_position], b_position: rules[b_position]}

    while substitutes_list:
        rules = delete_substitutes(rules, substitutes_list)
        rules = substitute_rules(rules, substitutes_list)
        substitutes_list = find_substitutes(rules)

    print('    - Correct rules with loop')
    rules = correct_rest_of_rules(rules)

    print('    - Find last substitutes')
    substitutes_list = find_substitutes(rules)

    print('    - Delete last substitutes from set of rules')
    rules = delete_substitutes(rules, substitutes_list)

    print('    - Put substitutes in main rule')
    rules = substitute_rules(rules, substitutes_list)

    print('    - Find all correct messages')
    number_correct_messages = find_correct_messages(rules['0'], messages)

    return number_correct_messages


def day_19_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name
    rules, messages = read_input_file(path_to_input)
    answer_1 = first_part(rules, messages)
    print('Your puzzle answer for first part is {0}'.format(answer_1))

    path_to_input = folder_name + '/' + file_name.split('.txt')[0] + '_part2.txt'
    rules, messages = read_input_file(path_to_input)
    answer_2 = second_part(rules, messages)
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_19_solution(input_folder_name, input_file_name)