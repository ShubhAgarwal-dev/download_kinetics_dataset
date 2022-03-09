# Work in progress
from batches import change_path
from get_data import get_start_by_name as gsn, get_end_by_name as ges
from moviepy.editor import *

import pathlib
import os


def refine_videos(batch_name, json_file):
    cp = change_path(batch_name)
    for path in pathlib.Path(cp).iterdir():
        file_tail = os.path.split(path)[1]
        file_name = os.path.splitext[file_tail][0]
        file_ext = os.path.splitext[file_tail][1]
        clip = VideoFileClip(f"{file_name}{file_ext}")
        start = gsn(batch_name, json_file)
        end = ges(batch_name, json_file)
        clip = clip.subclip(int(start), int(end))


if __name__ == '__main__':
    refine_videos('folder1')
