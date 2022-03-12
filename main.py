from batches import make_batch, download_batch
from video_trim import refine_videos, extract_frames

batch1 = make_batch(32, r'dataset2\validate.json')
download_batch(batch=batch1, name='folder2')
refine_videos(batch_name='folder2',
              json_file=r'D:\Projects\Inter-IIT\yt_video_downloader\dataset2\validate.json',
              audio=False)
extract_frames('folder2', 5)
