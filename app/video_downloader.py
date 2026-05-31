import yt_dlp
import os


def download_video(url):

    os.makedirs("videos", exist_ok=True)

    ydl_opts = {
        "format": "mp4",
        "outtmpl": "videos/video.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return "videos/video.mp4"