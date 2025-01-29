import shutil
import os

FILES_DIR = "/Users/grant/MY_DEV/files"
all_files = ['d2.doc','t1.txt','t2.txt','i3.img','d1.doc', 't3.txt', 'd3.doc', 'i2.img', 'i1.img']

for file_name in all_files:
    file_path = os.path.join(FILES_DIR, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            # print(content)
    else:
        print(f"File '{file_path}' does not exist.")

def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"File '{source}' moved to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"Error: Source file '{source}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def sort_files():
    doc_files = []
    txt_files = []
    img_files = []

    for file_name in all_files:
        file_path = os.path.join(FILES_DIR, file_name)
        if file_name.endswith('.doc'):
            doc_files.append(file_path)
        elif file_name.endswith('.txt'):
            txt_files.append(file_path)
        elif file_name.endswith('.img'):
            img_files.append(file_path)

    print("DOC files:", doc_files)
    print("TXT files:", txt_files)
    print("IMG files:", img_files)