import json


def change_label(filepath: str):

    with open(filepath, mode='r') as file:
        file_dict = json.load(file)
        file.close()

    for i in file_dict.items():
        i[1]['downloaded'] = False

    with open(filepath, mode='w') as file:
        file.write(json.dumps(file_dict, indent=4, sort_keys=True))


if __name__ == '__main__':
    # change_label('test.json')
    # change_label('train.json')
    change_label('validate.json')
