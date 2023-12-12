import os
import shutil
from datetime import datetime, timedelta

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def is_file_recently_modified(file_path, time_threshold):
    current_time = datetime.now()
    file_stat = os.stat(file_path)
    modification_time = datetime.fromtimestamp(file_stat.st_mtime)
    creation_time = datetime.fromtimestamp(file_stat.st_ctime)

    return current_time - modification_time <= time_threshold or current_time - creation_time <= time_threshold

def update_files(files):
    for file in files:
        try:
            with open(file, 'a') as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f'\nUpdated at {timestamp}')
        except Exception as e:
            print(f"Error updating file {file}: {e}")

def create_last_24hours_folder(folder_name):
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
    except Exception as e:
        print(f"Error creating folder {folder_name}: {e}")

def move_files_to_folder(files, destination_folder):
    try:
        for file in files:
            shutil.move(file, os.path.join(destination_folder, file))
    except Exception as e:
        print(f"Error moving files to {destination_folder}: {e}")

def main():
    try:
        current_directory = os.getcwd()
        last_24hours_folder = "last_24hours"

        files = list_files(current_directory)
        print("All files:", files)

        time_threshold = timedelta(hours=24)
        recent_files = [file for file in files if is_file_recently_modified(file, time_threshold)]
        print("Recently modified or created files:", recent_files)

        update_files(recent_files)

        create_last_24hours_folder(last_24hours_folder)
        
        move_files_to_folder(recent_files, last_24hours_folder)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
