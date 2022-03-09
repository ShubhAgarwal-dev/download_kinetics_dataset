import get_data
import json

import download
import os
import shutil


def prepare_json(json_file: str):
    with open(json_file, mode='r') as jsonfile:
        json_dict = json.load(jsonfile)
        jsonfile.close()
    return json_dict


def sync_changes(json_file, dict_data):
    with open(json_file, mode='w') as file:
        file.write(json.dumps(dict_data, indent=4, sort_keys=True))


def make_batch_labelwise(size: int, dataset: str, label: str):
    json_dict = prepare_json(dataset)
    batch = {}
    for j in range(size):
        for i in json_dict.items():
            if get_data.get_download_status(i):
                if get_data.get_class(i) == label:
                    batch.update(i)
                    i[1]['downloaded'] = True
    sync_changes(dataset, json_dict)
    return batch


def make_batch(size: int, dataset: str):
    json_dict = prepare_json(dataset)
    batch = []
    for i in json_dict.items():
        if len(batch) > size:
            break
        if not get_data.get_download_status(i):
            batch.append(get_data.get_name(i))
            i[1]['downloaded'] = True
    sync_changes(dataset, json_dict)
    return batch


def change_path(name):
    current_path = os.getcwd()
    path_to_save_to = current_path + fr'\destination\{name}'
    if not os.path.exists(path_to_save_to):
        os.makedirs(path_to_save_to)
    os.chdir(path_to_save_to)
    return path_to_save_to


def download_batch(batch, name):
    change_path(name)
    urls = get_data.get_urls_from_names(batch)
    with open('../batches.txt', mode='a+') as file:
        file.write(name+'\n')
        file.close()
    for i, url in enumerate(urls):
        print(url)
        # download.download_video(url, f'{batch[i]}.mp4', format='160')
        try:
            download.download_video(url, f'{batch[i]}.mp4', format='160')
        except:
            continue


def remove_batch(name):
    '''
    Please run command prompt as administrator
    '''
    current_path = change_path(name)
    path_tail = os.path.split(current_path)
    os.chdir(path_tail[0])
    # os.remove(current_path) # can only delete empty path
    shutil.rmtree(current_path)


if __name__ == '__main__':
    a = make_batch(32, r'dataset2/validate.json')
    download_batch(a, 'folder1')
