# Work in progress
from batches import change_path
from get_data import get_start_by_name as gsn, get_end_by_name as ges
from moviepy.editor import *

import pathlib
import os

import numpy as np
from datetime import timedelta


def refine_videos(batch_name, json_file, audio=False):
    """
    To get the videos of desired length
    """
    cp = change_path(batch_name)
    for path in pathlib.Path(cp).iterdir():
        # file_tail = os.path.split(path)[1]
        # file_name = os.path.splitext[file_tail][0]
        # file_ext = os.path.splitext[file_tail][1]
        file_name_ht = os.path.split(path)
        file_name_split_ht = os.path.splitext(file_name_ht[1])
        file_name = file_name_split_ht[0]
        file_ext = file_name_split_ht[1]
        clip = VideoFileClip(f"{file_name}{file_ext}")
        start = gsn(file_name, json_file)
        end = ges(file_name, json_file)
        clip = clip.subclip(int(start), int(end))
        clip.write_videofile(str(path), audio=audio)


# Below it the code to extract frames from the video
def format_timedelta(td):
    """Utility function to format timedelta objects in a cool way (e.g 00:00:20.05) 
    omitting microseconds and retaining milliseconds"""
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return result + ".00".replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")


def extract_frames(video_file, FPS):
    """
    To extract frames from the video_file 
    and FPS is the frames you want
    """
    # load the video clip
    video_clip = VideoFileClip(video_file)
    # make a folder by the name of the video file
    filename, _ = os.path.splitext(video_file)
    if not os.path.isdir(filename):
        os.mkdir(filename)

    # if the SAVING_FRAMES_PER_SECOND is above video FPS, then set it to FPS (as maximum)
    saving_frames_per_second = min(video_clip.fps, FPS)
    # if SAVING_FRAMES_PER_SECOND is set to 0, step is 1/fps, else 1/SAVING_FRAMES_PER_SECOND
    step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / \
        saving_frames_per_second
    # iterate over each possible frame
    for current_duration in np.arange(0, video_clip.duration, step):
        # format the file name and save it
        frame_duration_formatted = format_timedelta(
            timedelta(seconds=current_duration)).replace(":", "-")
        frame_filename = os.path.join(
            filename, f"frame{frame_duration_formatted}.jpg")
        # save the frame with the current duration
        video_clip.save_frame(frame_filename, current_duration)


if __name__ == '__main__':
    # refine_videos('folder1')
    refine_videos('fld3', '../../dataset2/validate.json')
