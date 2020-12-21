from sys import argv
from os import chdir


def read_rules(text):

    rules = dict()

    for line in text:
        rule_type = line.split(':')[0].strip()

        rule_text = line.split(':')[1].strip().split('or')
        rule_first_part = rule_text[0].strip().split('-')
        rule_first_part = (int(rule_first_part[0]), int(rule_first_part[1]))
        rule_second_part = rule_text[1].strip().split('-')
        rule_second_part = (int(rule_second_part[0]), int(rule_second_part[1]))

        rules[rule_type] = [rule_first_part, rule_second_part]

    return rules


def read_tickets(text):

    tickets = list()
    for ticket_i in text:
        current_ticket = ticket_i.split(',')
        current_ticket = [int(current_ticket[i]) for i in range(len(current_ticket))]
        tickets.append(current_ticket)

    return tickets


def read_input_file(path_to_file):

    input_data = open(path_to_file, 'r').read()
    rules_text = input_data.split('your ticket:')[0].strip().split('\n')
    your_ticket_text = [input_data.split('your ticket:')[1].split('nearby tickets:')[0].strip()]
    nearby_tickets_text = input_data.split('your ticket:')[1].split('nearby tickets:')[1].strip().split()

    rules = read_rules(rules_text)
    your_ticket = read_tickets(your_ticket_text)
    nearby_tickets = read_tickets(nearby_tickets_text)

    return rules, your_ticket, nearby_tickets


def first_part(rules, nearby_tickets):

    incorrect_fields = list()
    valid_tickets = list()

    for ticket in nearby_tickets:
        valid_fields = list()
        for field in ticket:
            not_valid = list()
            for rule in rules.keys():
                rule_limits = rules[rule]
                if not ((rule_limits[0][0] <= field <= rule_limits[0][1]) or (rule_limits[1][0] <= field <= rule_limits[1][1])):
                    not_valid.append(True)
                else:
                    break

            if len(not_valid) == len(rules.keys()):
                incorrect_fields.append(field)
            else:
                valid_fields.append(True)

        if len(valid_fields) == len(ticket):
            valid_tickets.append(ticket)

    answer = sum(incorrect_fields)

    return answer, valid_tickets


def second_part(rules, your_ticket, valid_tickets):

    tickets_and_meanings = dict()

    count_tickets = 0
    for ticket in valid_tickets:
        possible_meanings = dict()
        for field_i in range(len(ticket)):
            meanings = list()
            field = ticket[field_i]
            for rule in rules.keys():
                rule_limits = rules[rule]
                if (rule_limits[0][0] <= field <= rule_limits[0][1]) or (rule_limits[1][0] <= field <= rule_limits[1][1]):
                    meanings.append(rule)
            possible_meanings[field_i] = meanings
        tickets_and_meanings[count_tickets] = possible_meanings
        count_tickets += 1

    tickets_number = len(tickets_and_meanings.keys())
    fields_number = len(tickets_and_meanings[0].keys())

    all_sets = dict()

    for field_i in range(fields_number):
        results_set = set(tickets_and_meanings[0][field_i])
        for ticket_i in range(1, tickets_number):
            new_set = set(tickets_and_meanings[ticket_i][field_i])
            intersection = results_set.intersection(new_set)
            results_set = intersection
        all_sets[field_i] = results_set


    defined = list()
    max_field_lenght = max([len(all_sets[field]) for field in all_sets.keys()])
    while max_field_lenght != 0:
        defined_field_index = [field for field in all_sets.keys() if len(all_sets[field]) == 1][0]
        defined_field_meaning = list(all_sets[defined_field_index])[0]
        defined.append((defined_field_index, defined_field_meaning))
        all_sets.pop(defined_field_index)

        for field_i in all_sets:
            all_sets[field_i].remove(defined_field_meaning)

        if all_sets:
            max_field_lenght = max([len(all_sets[field]) for field in all_sets.keys()])
        else:
            max_field_lenght = 0

    answer = 1
    for pair in defined:
        if pair[1].startswith('departure'):
            answer *= your_ticket[0][pair[0]]

    return answer


def day_16_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    rules, your_ticket, nearby_tickets = read_input_file(path_to_input)

    answer_1, valid_tickets = first_part(rules, nearby_tickets)
    answer_2 = second_part(rules, your_ticket, valid_tickets)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_16_solution(input_folder_name, input_file_name)