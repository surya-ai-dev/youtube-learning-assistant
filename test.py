# from app.transcript import get_transcript

# url = input("Enter YouTube URL: ")

# text = get_transcript(url)

# print(text[:1000])



from app.transcript import get_transcript
from app.summarizer import summarize_text
from app.pdf_generator import generate_pdf
from app.video_downloader import download_video


# url = input("Enter YouTube URL: ")

# transcript = get_transcript(url)

# print("Transcript fetched successfully")

# summary = summarize_text(transcript)

# print("\nSUMMARY\n")
# print(summary)


# pdf_file = generate_pdf(summary)

# print(f"PDF Generated: {pdf_file}")



#----->Video download Test--->
# url = input("Enter URL: ")

# video_path = download_video(url)

# print(video_path)


###------------ Frame Extracter Test----->
# from app.frame_extractor import extract_frames

# video_path = "videos/video.mp4"

# num_frames = extract_frames(
#     video_path,
#     interval_seconds=10
# )

# print(f"Frames Extracted: {num_frames}")


#---> Remove duplicate Frames
from app.frame_filter import remove_duplicate_frames

frames = remove_duplicate_frames()

print(f"Unique Frames: {len(frames)}")

for frame in frames:
    print(frame)
