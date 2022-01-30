import json
from typing import List, Dict, Any


def path_cleaner(path) -> str:
    path_encode = path.encode('ascii', 'ignore')
    path_decode = path_encode.decode()
    new_path = path_decode.replace('\\', '/')
    return new_path


def formatting(csv_file, name) -> Dict[Any, List[Any]]:
    arr = {name: []}
    for row in csv_file:
        arr[name].append(row)
    return arr


def to_json_convert(csv_file, name):
    arr = formatting(csv_file, name)
    json_string = json.dumps(arr, indent=4)
    with open(f'{name}.json', 'w') as json_file:
        json_file.write(json_string)
        json_file.close()


def to_yaml_convert(csv_file, name):
    arr = formatting(csv_file, name)
    with open(f'{name}.yaml', 'w') as yaml_file:
        yaml_file.write(f'{name}:\n')
        for row in arr[name]:
            for count, value in enumerate(row):
                if count != 0:
                    yaml_file.write(f'    {value}: {row[value]}\n')
                else:
                    yaml_file.write(f'  - {value}: {row[value]}\n')
        yaml_file.close()
