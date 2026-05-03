import os
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from config import BASE_DIR, DESTINATIONS
from classifier import classify_file


def wait_until_ready(file_path):
    while True:
        try:
            with open(file_path, "rb"):
                return
        except:
            time.sleep(1)


def move_file(src, category):
    dest_folder = DESTINATIONS[category]

    os.makedirs(dest_folder, exist_ok=True)

    filename = os.path.basename(src)
    dest_path = os.path.join(dest_folder, filename)

    # handle duplicates
    base, ext = os.path.splitext(dest_path)
    counter = 1

    while os.path.exists(dest_path):
        dest_path = f"{base}_{counter}{ext}"
        counter += 1

    try:
        os.rename(src, dest_path)
        return dest_path
    except Exception as e:
        print("Move failed:", e)
        return None


class FileHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path

        if file_path.endswith((".crdownload", ".tmp", ".part")):
            return

        print(f"\nNew file: {file_path}")

        wait_until_ready(file_path)

        category = classify_file(file_path)

        new_path = move_file(file_path, category)

        if new_path:
            print(f"Moved → {new_path}")


def start_watcher():
    observer = Observer()
    observer.schedule(FileHandler(), path=BASE_DIR, recursive=False)
    observer.start()

    print("File organizer running...")

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


# run directly
start_watcher()