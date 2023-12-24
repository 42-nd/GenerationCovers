"""Just a small script that I personally needed to transfer in chunks to Google drive"""

import os
import shutil


def split_files(source_folder, destination_folder, batch_size=5000):
    os.makedirs(destination_folder, exist_ok=True)

    files = os.listdir(source_folder)

    batches = [files[i : i + batch_size] for i in range(0, len(files), batch_size)]

    for i, batch in enumerate(batches):
        batch_folder = os.path.join(destination_folder, f"batch_{i + 1}")
        os.makedirs(batch_folder, exist_ok=True)

        for file_name in batch:
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(batch_folder, file_name)
            shutil.copy2(source_path, destination_path)


if __name__ == "__main__":
    source_folder = ""
    destination_folder = ""

    split_files(source_folder, destination_folder)
