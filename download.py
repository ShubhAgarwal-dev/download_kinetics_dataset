from __future__ import unicode_literals
import youtube_dl


def download_video(link: str, name: str, format='22/18/160'):
    """
    Refer to youtube format code tags for specifying the format
    """
    ydl_opts = {'format': format, 'outtmpl': name}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        link_list = []
        link_list.append(link)
        ydl.download(link_list)
