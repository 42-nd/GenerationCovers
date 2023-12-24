"""Actually, it's not the best way to download images, 
but for 1000x1000 images in the size of 60,000 pieces, it took about 12 hours to download, 
for 120,000 200x200 it took about 3 days"""


from yandex_music import Client
import random
import os
import time
from PIL import Image

TOKEN = ""
LOWER_BOUND = 1
UPPER_BOUND = 28858479
THRESHOLD_IMAGES_PER_GENRE = 500
FOLDER_PATH = r""
SIZE = (256, 256)


def download_album_cover(album_id, downloaded_counter):
    try:
        album = client.albums_with_tracks(album_id)
        if album.cover_uri is not None and album.genre is not None:
            genre = album.genre
            album.download_cover(
                filename=f"{FOLDER_PATH}\{album_id}_{genre}.jpg",
                size="1000x1000",
            )
            print(f"Already downloaded: {downloaded_counter} covers")
            return 1
        else:
            return 0
    except Exception as e:
        print(f"Error downloading album {album_id}: {str(e)}")
        return -1


client = Client(TOKEN).init()
generated_numbers = set()
genre_counter = {}
genre_files = {}
existing_albums = set()


for filename in os.listdir(FOLDER_PATH):
    album_id, genre = map(str, filename.split("_")[:2])

    genre_mapping = {  # Here are the most significant genres in my opinion, the rest are too few for them to have any meaning.
        "latinfolk": "folk",
        "foreignrap": "rap",
        "rusrap": "rap",
        "trance": "electronics",
        "reggaeton": "reggae",
        "ruspop": "pop",
        "metal": "rock",
        "folkgenre": "folk",
        "ambientgenre": "relax",
        "punk": "rock",
        "lounge": "relax",
        "dnb": "electronics",
        "arabicpop": "pop",
        "vocaljazz": "jazz",
        "kpop": "pop",
        "rusrock": "rock",
        "tradjazz": "jazz",
        "classicmetal": "rock",
        "dubstep": "electronics",
        "ska": "reggae",
        "eurofolk": "folk",
        "meditation": "relax",
        "conjazz": "jazz",
        "classicalmasterpieces": "classical",
        "local-indie": "indie",
        "turkishpop": "pop",
        "turkishfolk": "folk",
        "turkishrap": "rap",
        "hardrock": "rock",
        "japanesepop": "pop",
        "foreignbard": "bard",
        "blues": "soul",
        "bebopgenre": "jazz",
        "funk": "soul",
    }

    # # RENAMING AND MERGING
    # try:
    #     modified_genre = genre_mapping[genre[:-4]]
    #     original_path = os.path.join(FOLDER_PATH, filename)
    #     new_filename = f"{album_id}_{modified_genre}.jpg"
    #     new_path = os.path.join(FOLDER_PATH, new_filename)
    #     os.rename(original_path, new_path)
    # except:
    #     pass

    existing_albums.add(album_id)
    genre_counter[genre] = genre_counter.get(genre, 0) + 1

    # GETTING PATHS BY GENRES
    if genre[:-4] not in genre_files:
        genre_files[genre[:-4]] = []
    genre_files[genre[:-4]].append(filename)


genre_counter = dict(sorted(genre_counter.items(), key=lambda x: x[1], reverse=True))
print("Downloaded images per genre:")
for genre, count in genre_counter.items():
    print(f"{genre}: {count}")

downloaded_counter = len(existing_albums) + 1
print("Total downloaded :", downloaded_counter)


# # RESIZE
# for file_name in os.listdir(FOLDER_PATH):
#     if file_name.endswith(".jpg") or file_name.endswith(".png"):
#         img_path = os.path.join(FOLDER_PATH, file_name)
#         img = Image.open(img_path)
#         img = img.convert("RGB")
#         img = img.resize(SIZE)
#         img.save(img_path)


# # DOWNLOADING IMAGES
# while downloaded_counter != 150000 + 1:
#     random_number = random.randint(LOWER_BOUND, UPPER_BOUND)
#     while random_number in generated_numbers or random_number in existing_albums:
#         random_number = random.randint(LOWER_BOUND, UPPER_BOUND)
#     generated_numbers.add(random_number)
#     album_id = random_number

#     success = download_album_cover(album_id, downloaded_counter)
#     if success == 1:
#         downloaded_counter += 1
#     elif success == -1:
#         time.sleep(5)

# # DELETING BY THRESHOLD
# for genre, count in genre_counter.items():
#     if count < THRESHOLD_IMAGES_PER_GENRE and genre[:-4] in genre_files:
#         for file in genre_files[genre[:-4]]:
#             # print(file, genre_files[genre[:-4]])
#             file_path = os.path.join(FOLDER_PATH, file)
#             os.remove(file_path)
#             print(f"Deleted file: {file}")
#         del genre_files[genre[:-4]]
#         print(f"Deleted all files for genre {genre} (below threshold)")

# DELETING BY GENRE
# genre_to_delete = "children"
# if genre_to_delete in genre_files:
#     for file in genre_files[genre_to_delete]:
#         file_path = os.path.join(FOLDER_PATH, file)
#         os.remove(file_path)
#         # print(f"Deleted file: {file}")
#     del genre_files[genre_to_delete]
#     print(f"Deleted all files for genre: {genre_to_delete}")
