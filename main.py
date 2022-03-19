from __future__ import unicode_literals
import os
from video_trim import batch_frame_extractor, refine_videos, extract_frames
from batches import clean_up_dir, make_batch, download_batch

import json

cdir = os.getcwd()

# batch1 = make_batch(16, r'dataset2\validate.json')
# # os.chdir(cdir)
# download_batch(batch=batch1, name='folder8')
# os.chdir(cdir)
# clean_up_dir('folder8')
# os.chdir(cdir)
# refine_videos(batch_name='folder8',
#               json_file=r'D:\Projects\Inter-IIT\yt_video_downloader\dataset2\validate.json',
#               audio=True)
# os.chdir(cdir)
# batch_frame_extractor('folder8', 3)


def automater(name: str, json_file: str, count: int = 16, fps: int = 5):
    json_file_loc = fr'D:\Projects\Inter-IIT\yt_video_downloader\dataset2\{json_file}'
    batch = make_batch(count, json_file_loc)
    download_batch(batch, name)
    os.chdir(cdir)
    refine_videos(str(name), json_file_loc)
    os.chdir(cdir)
    batch_frame_extractor(name, fps)


def download_video(dataset, name, count=2):
    batch = make_batch(count, dataset)
    download_batch(batch, name)
    os.chdir(cdir)
    refine_videos(name, dataset)


def change_label(filepath: str):
    '''
    Please run to add 'download' key to
    your json file, otherwise it may not make a 
    '''
    with open(filepath, mode='r') as file:
        file_dict = json.load(file)
        file.close()

    for i in file_dict.items():
        i[1]['downloaded'] = False

    with open(filepath, mode='w') as file:
        file.write(json.dumps(file_dict, indent=4, sort_keys=True))


1
if __name__ == '__main__':
    # automater('fld1', 'validate.json', count=128, fps=10) # Do not run this

    # change_label('train1.json')
    # # Please run this before using new json file
    # #it is required to add download key to json file
    # #which is required before making batches

    download_video(
        r'D:\Projects\Inter-IIT\yt_video_downloader\train1.json', 'train1')
