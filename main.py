from __future__ import unicode_literals
import os
from video_trim import batch_frame_extractor, refine_videos, extract_frames
from batches import clean_up_dir, make_batch, download_batch

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


if __name__ == '__main__':
    # automater('fld1', 'validate.json', count=128, fps=10)
    download_video('train1.json', 'train1')
