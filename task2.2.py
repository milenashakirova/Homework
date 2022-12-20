import os

filename = input("Введите название файла(csv): ")

check_bool = {'True': 'true', "False": 'false', '': 'null'}


def str_split(string):
    return string.split(',')


with open(filename, 'r', encoding='utf-8') as infile, \
        open('output_test.json', 'w', encoding='utf-8') as outfile:

    data = []

    if os.path.getsize(filename):
        data = '[\n'
        header, *strings = list(map(str_split, map(str.strip, infile.readlines())))

        for ind, line in enumerate(strings):
            data += '  {\n'

            for index, elem in enumerate(line, 0):

                if index == len(line) - 1:
                    if elem in check_bool:
                        elem = check_bool[elem]
                        data += f'    "{header[index]}": {elem}\n'
                    else:
                        data += f'    "{header[index]}": "{elem}"\n'
                else:
                    if elem in check_bool:
                        elem = check_bool[elem]
                        data += f'    "{header[index]}": {elem},\n'
                    else:
                        data += f'    "{header[index]}": "{elem}",\n'

            if ind == len(strings) - 1:
                data += '  }\n'
            else:
                data += '  },\n'

        data += ']'

    print(data, file=outfile, end='')