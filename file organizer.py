import os
import shutil

def auto_sort_files_by_extension(directory):
    os.chdir(directory)

    for file in os.listdir():
        if os.path.isdir(file):
            continue

        file_name, file_ext = os.path.splitext(file)

        if not file_ext:
            continue
        folder_name = file_ext[1:].lower()

        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        shutil.move(file, os.path.join(folder_name, file))

    print(f"Files in '{directory}' have been sorted by extension.")

folder_path = input("Enter the path to the folder you want to sort: ").strip()

if os.path.exists(folder_path):
    auto_sort_files_by_extension(folder_path)
else:
    print("Invalid folder path.")