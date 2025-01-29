import shutil
import os

FILES_DIR = "/Users/grant/MY_DEV/files"
all_files = ['d2.doc','t1.txt','t2.txt','i3.img','d1.doc', 't3.txt', 'd3.doc', 'i2.img', 'i1.img']
for i in range(0,len(all_files)):
    f_nm = FILES_DIR + "/" + all_files[i]
    with open(f_nm,'r') as file:
        content = file.read()
        # print(content)
        
def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"File '{source}' moved to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"Error: Source file '{source}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def sort_files():
    for i in range(0,len(all_files)):
        f_nm = FILES_DIR + "/" + all_files[i]
        print(f"f_nm = ", f_nm)
        if '.txt' in f_nm:
            print(f"f_nm = ", f_nm)
            move_file(f_nm, '/Users/grant/MY_DEV/texts')
        elif '.doc' in f_nm:
            print(f"f_nm = ", f_nm)
            move_file(f_nm, '/Users/grant/MY_DEV/docs')
        else:
            print(f"f_nm = ", f_nm)
            move_file(f_nm, '/Users/grant/MY_DEV/images')

if __name__ == "__main__":
    sort_files()