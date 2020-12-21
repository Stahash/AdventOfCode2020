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

    for ticket in nearby_tickets:
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

    answer = sum(incorrect_fields)

    return answer


def second_part(rules, your_ticket):


    return None


def day_16_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    rules, your_ticket, nearby_tickets = read_input_file(path_to_input)

    answer_1 = first_part(rules, nearby_tickets)
    answer_2 = second_part(rules, your_ticket)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_16_solution(input_folder_name, input_file_name)