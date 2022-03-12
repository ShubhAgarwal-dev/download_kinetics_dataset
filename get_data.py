import json


def get_urls_from_names(itter):
    urls = []
    for i in itter:
        urls.append(f'https://www.youtube.com/watch?v={i}')
    return urls


def prepare_json(json_file: str = r'dataset2/test.json'):
    with open(json_file, mode='r') as jsonfile:
        json_dict = json.load(jsonfile)
        jsonfile.close()
    return json_dict


def get_start(json_item):
    return json_item[1]['annotations']['segment'][0]


def get_end(json_item):
    return json_item[1]['annotations']['segment'][1]


def get_link(json_item):
    return json_item[1]['url']


def get_class(json_item):
    return json_item[1]['annotations']['label']


def get_download_status(json_item):
    return json_item[1]['downloaded']


def get_name(json_item):
    return json_item[0]


def get_start_by_name(name, json_file):
    json_dict = prepare_json(json_file)
    req_value = json_dict[name]
    return req_value['annotations']['segment'][0]


def get_end_by_name(name, json_file):
    json_dict = prepare_json(json_file)
    req_value = json_dict[name]
    return req_value['annotations']['segment'][1]
