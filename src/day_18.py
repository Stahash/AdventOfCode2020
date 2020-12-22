from sys import argv
from os import chdir
from functools import reduce


def read_input_file(path_to_file):

    input_data = open(path_to_file, 'r').readlines()
    input_data = [line.strip() for line in input_data]

    return input_data


def find_parentheses(example):

    open_parentheses = list()
    parentheses_positions = list()

    for symbol_index in range(len(example)):
        symbol = example[symbol_index]
        if symbol == '(':
            open_parentheses.append(symbol_index)
        if symbol == ')':
            parentheses_positions.append((open_parentheses[-1], symbol_index))
            del open_parentheses[-1]

    return parentheses_positions


def calculate_inside_paretheses(elementary_expression):

    elements = elementary_expression.split(' ')
    updated_elements = elements.copy()
    result = 0

    while len(updated_elements) > 1:
        first = int(updated_elements[0])
        sign = updated_elements[1]
        second = int(updated_elements[2])

        if sign == '+':
            result = first + second
        elif sign == '*':
            result = first * second

        updated_elements = updated_elements[3:]
        updated_elements.insert(0, result)

    return result


def addition_first(elementary_expression):

    elements = elementary_expression.split(' ')
    updated_elements = elements.copy()

    pluses_indexes = [index for index in range(len(elements)) if elements[index] == '+']
    while pluses_indexes:
        first = int(updated_elements[pluses_indexes[0] - 1])
        second = int(updated_elements[pluses_indexes[0] + 1])
        result = first + second
        intermediate_list = list()
        intermediate_list = intermediate_list + updated_elements[0:pluses_indexes[0] - 1]
        intermediate_list.append(result)
        intermediate_list = intermediate_list + updated_elements[pluses_indexes[0]+2:]
        pluses_indexes = [index for index in range(len(intermediate_list)) if intermediate_list[index] == '+']
        updated_elements = intermediate_list.copy()

    updated_elements = [int(element) for element in updated_elements if element != '*']
    result = reduce(lambda x, y: x*y, updated_elements)

    return result


def change_expression(put_value, parentheses_borders, expression):
    changed_expression = expression[0:parentheses_borders[0]] + str(put_value) + expression[parentheses_borders[1]+1:]
    return changed_expression


def first_part(data):

    expression_results = list()
    for expression in data:

        current_expression = expression
        parentheses = find_parentheses(expression)

        while parentheses:
            borders = parentheses[0]
            value_inside = calculate_inside_paretheses(current_expression[borders[0]+1:borders[1]])
            new_expression = change_expression(value_inside, borders, current_expression)
            parentheses = find_parentheses(new_expression)
            current_expression = new_expression

        expression_value = calculate_inside_paretheses(current_expression)
        expression_results.append(expression_value)

    answer = sum(expression_results)
    return answer


def second_part(data):

    expression_results = list()
    for expression in data:

        current_expression = expression
        parentheses = find_parentheses(expression)

        while parentheses:
            borders = parentheses[0]
            value_inside = addition_first(current_expression[borders[0] + 1:borders[1]])
            new_expression = change_expression(value_inside, borders, current_expression)
            parentheses = find_parentheses(new_expression)
            current_expression = new_expression

        expression_value = addition_first(current_expression)
        expression_results.append(expression_value)

    answer = sum(expression_results)

    return answer


def day_18_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    input_data = read_input_file(path_to_input)

    answer_1 = first_part(input_data)
    answer_2 = second_part(input_data)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_18_solution(input_folder_name, input_file_name)