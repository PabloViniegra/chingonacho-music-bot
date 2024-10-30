from pytube import Search
import os
import shutil
import yt_dlp


def give_link(name):
    s = Search(name)
    video_ids = [video.video_id for video in s.results]

    if video_ids:
        video_id = video_ids[0]
        return f"https://www.youtube.com/watch?v={video_id}"
    return None


def download_vid(name):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'outtmpl': 'music/%(title)s.%(ext)s',
            'quiet': True,
            'ffmpeg_location': 'C:/ffmpeg',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{name}", download=True)
            video_title = info['entries'][0]['title']
            return f"{video_title}.mp3"

    except Exception as e:
        print(f"Error downloading audio: {e}")
        return None


def delete_audio():
    if os.path.exists('music'):
        shutil.rmtree('music')


def find_music_name():
    return os.listdir("music")[0] if os.path.exists("music") and os.listdir("music") else None


def remove_all_files(dir):
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
