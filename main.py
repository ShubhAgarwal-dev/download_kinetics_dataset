from email.mime import audio
from batches import clean_up_dir, make_batch, download_batch
from video_trim import batch_frame_extractor, refine_videos, extract_frames
import os

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


def automater(name: str, json_file: str, count: int = 16, audio: bool = True, fps: int = 5):
    json_file_loc = fr'D:\Projects\Inter-IIT\yt_video_downloader\dataset2\{json_file}'
    batch = make_batch(count, json_file_loc)
    download_batch(batch, name)
    os.chdir(cdir)
    refine_videos(name, json_file_loc, audio)
    os.chdir(cdir)
    batch_frame_extractor(name, fps)


if __name__ == '__main__':
    automater('folder11', 'validate.json', audio=False)
