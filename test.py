# from app.transcript import get_transcript

# url = input("Enter YouTube URL: ")

# text = get_transcript(url)

# print(text[:1000])



from app.transcript import get_transcript
from app.summarizer import summarize_text

url = input("Enter YouTube URL: ")

transcript = get_transcript(url)

print("Transcript fetched successfully")

summary = summarize_text(transcript)

print("\nSUMMARY\n")
print(summary)