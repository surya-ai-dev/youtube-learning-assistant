import os
import shutil
from PIL import Image
import imagehash

os.makedirs(
    "unique_frames",
    exist_ok=True
)
def remove_duplicate_frames(
    frame_folder="frames",
    threshold=5
):

    unique_frames = []

    hashes = []

    files = sorted(os.listdir(frame_folder))

    for file in files:

        path = os.path.join(frame_folder, file)

        image = Image.open(path)

        current_hash = imagehash.phash(image)

        duplicate = False

        for existing_hash in hashes:

            if abs(current_hash - existing_hash) <= threshold:
                duplicate = True
                break

        if not duplicate:

            hashes.append(current_hash)

            unique_frames.append(path)
            destination = os.path.join(
                "unique_frames",
                file
            )

            shutil.copy(
                path,
                destination
            )

    return unique_frames