import csv

from services import path_cleaner, to_json_convert, to_yaml_convert


def converter(path, delimiter):
    formatted_path = path_cleaner(path)

    with open(formatted_path, newline='') as csv_file:

        new_file = csv.DictReader(csv_file,
                                  delimiter=delimiter,
                                  quoting=csv.QUOTE_ALL)

        convert_format = new_file.fieldnames.pop(-1)
        name = csv_file.name.split('/')[-1][:-4]

        if convert_format == 'json':
            to_json_convert(new_file, name)
        elif convert_format == 'yaml':
            to_yaml_convert(new_file, name)
        else:
            print('There should be a converting format in the first line')
