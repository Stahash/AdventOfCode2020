from sys import argv
from os import chdir


def read_input_file(data):
    all_passports = dict()
    fields_in_passport = dict()
    passport_index = 0
    for current_line in data:
        line_index = data.index(current_line)

        if current_line != '':
            current_line_data = current_line.split(' ')
            for data_i in current_line_data:
                data_i = data_i.split(':')
                fields_in_passport[data_i[0]] = data_i[1]

            if line_index == len(data) - 1:
                passport_index += 1
                all_passports[passport_index] = fields_in_passport
        else:
            passport_index += 1
            all_passports[passport_index] = fields_in_passport
            fields_in_passport = dict()

    return all_passports


def first_part(passports_data):

    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
    optional_fields = {'cid'}

    valid_passports = 0
    valid_passports_indexes = list()

    for passport_number in passports_data.keys():
        fields_in_current_passport = set(passports_data[passport_number].keys())
        if fields_in_current_passport == required_fields:
            valid_passports += 1
            valid_passports_indexes.append(passport_number)
        elif required_fields.difference(fields_in_current_passport) == optional_fields:
            valid_passports += 1
            valid_passports_indexes.append(passport_number)
        else:
            difference = required_fields.difference(fields_in_current_passport)
            print('Passport number {0} is invalid. Required fields {1} are missed'
                  .format(passport_number, difference))

    return valid_passports, valid_passports_indexes


def second_part(passports_data, valid_passports_indexes):
    legal_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    legal_hair_color_symbols = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}
    truly_valid_passports = 0
    for passport_i in passports_data.keys():
        valid_fields = list()
        current_passport = passports_data[passport_i]

        if passport_i in valid_passports_indexes:

            # byr (Birth Year) - four digits; at least 1920 and at most 2002.
            Birth_Year = int(current_passport['byr'])
            if (Birth_Year >= 1920) and (Birth_Year <= 2002):
                valid_fields.append('True')
            else:
                print('Passport {0} is invalid because of byr = {1}'.format(passport_i, Birth_Year))

            # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            Issue_Year = int(current_passport['iyr'])
            if (Issue_Year >= 2010) and (Issue_Year <= 2020):
                valid_fields.append('True')
            else:
                print('Passport {0} is invalid because of iyr = {1}'.format(passport_i, Issue_Year))

            # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            Expiration_Year = int(current_passport['eyr'])
            if (Expiration_Year >= 2020) and (Expiration_Year <= 2030):
                valid_fields.append('True')
            else:
                print('Passport {0} is invalid because of eyr = {1}'.format(passport_i, Expiration_Year))

            # hgt(Height) - a number followed by either cm or in:
            # If cm, the number must be at least 150 and at most 193.
            # If in, the number must be at least 59 and at most 76.
            Height = current_passport['hgt']
            height_unit = Height[-2:]
            try:
                height_value = int(Height[0:-2])
                if height_unit == 'cm':
                    if (height_value >= 150) and (height_value <= 193):
                        valid_fields.append('True')
                elif height_unit == 'in':
                    if (height_value >= 59) and (height_value <= 76):
                        valid_fields.append('True')
            except:
                print('Passport {0}: {1} hgt value is incorrect'.format(passport_i, current_passport['hgt']))

            # hcl(Hair Color) - a  # followed by exactly six characters 0-9 or a-f.
            # hcl valid:   #123abc
            # hcl invalid: #123abz
            # hcl invalid: 123abc
            Hair_Color = current_passport['hcl']
            if Hair_Color[0] is '#':
                set_symbols = set(Hair_Color[1:])
                if len(Hair_Color) == 7:
                    if set_symbols.issubset(legal_hair_color_symbols) == True:
                        valid_fields.append('True')

            # ecl(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            Eye_Color = current_passport['ecl']
            if Eye_Color in legal_eye_colors:
                valid_fields.append('True')

            # pid(Passport ID) - a nine - digit number, including leading zeroes.
            Passport_ID = current_passport['pid']
            if len(Passport_ID) == 9:
                try:
                    Passport_ID = int(current_passport['pid'])
                    valid_fields.append('True')
                except:
                    print('Passport {0}: {1} pid value is incorrect'.format(passport_i, current_passport['pid']))

                    # cid(Country ID) - ignored, missing or not.

            if len(valid_fields) == 7:
                truly_valid_passports += 1

    return truly_valid_passports


def day_4_solution(folder_name, file_name):

    chdir('..')
    path_to_input = folder_name + '/' + file_name

    input_data = open(path_to_input, 'r').readlines()
    input_data = [input_data[i].rstrip() for i in range(len(input_data))]

    all_passports_data = read_input_file(input_data)
    answer_1, valid_passports = first_part(all_passports_data)
    answer_2 = second_part(all_passports_data, valid_passports)

    print('Your puzzle answer for first part is {0}'.format(answer_1))
    print('Your puzzle answer for second part is {0}'.format(answer_2))


if __name__ == "__main__":
    input_folder_name = argv[1]
    input_file_name = argv[2]
    day_4_solution(input_folder_name, input_file_name)