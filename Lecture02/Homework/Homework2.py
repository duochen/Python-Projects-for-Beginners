import os
import shutil
import datetime

# Define the directory to organize
directory = './TestData'

# Define file type categories
file_types = {
    'Images': ['jpg', 'jpeg', 'png', 'gif'],
    'Documents': ['pdf', 'docx', 'txt', 'xlsx'],
    'Videos': ['mp4', 'mkv', 'avi'],
    'Audio': ['mp3', 'wav']
}

# Function to create folders based on categories
def create_folders(base_path):
    for folder in file_types.keys():
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Function to organize files
def organize_files(base_path):
    for file_name in os.listdir(base_path):
        file_path = os.path.join(base_path, file_name)
        if os.path.isfile(file_path):
            ext = file_name.split('.')[-1].lower()
            folder_name = None
            for category, extensions in file_types.items():
                if ext in extensions:
                    folder_name = category
                    break
            if folder_name:
                new_folder_path = os.path.join(base_path, folder_name)
                new_file_path = os.path.join(new_folder_path, file_name)
                if os.path.exists(new_file_path):
                    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                    new_file_name = f"{timestamp}_{file_name}"
                    new_file_path = os.path.join(new_folder_path, new_file_name)
                shutil.move(file_path, new_file_path)

# Main script execution
if __name__ == "__main__":
    create_folders(directory)
    organize_files(directory)
    print("Files have been organized successfully.")
