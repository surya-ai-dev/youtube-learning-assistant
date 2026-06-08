from youtube_transcript_api import YouTubeTranscriptApi
import re


def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    
    print(f'Match after Extract:{match}')

    if match:
        return match.group(1)#-----?

    return None


def get_transcript(url):
    video_id = extract_video_id(url)
    print(f'Video_ID:{video_id}')
    ytt_api = YouTubeTranscriptApi()

    transcript = ytt_api.fetch(video_id)
    print(f'Transcript:{transcript}')
   

    text = " ".join(entry.text for entry in transcript)
    text = text[:30000]
  

    return text
