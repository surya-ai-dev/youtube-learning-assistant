import cv2
import os


def extract_frames(video_path, interval_seconds=10):

    os.makedirs("frames", exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)

    frame_interval = int(fps * interval_seconds)

    count = 0
    saved = 0

    while True:

        success, frame = cap.read()

        if not success:
            break

        if count % frame_interval == 0:

            frame_path = f"frames/frame_{saved}.jpg"

            cv2.imwrite(frame_path, frame)

            saved += 1

        count += 1

    cap.release()

    return saved