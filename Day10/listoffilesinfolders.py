import os

folder_name = input(
    "Please list of folder names with spaces in between:").split()


for folder in folder_name:
    try:
        files = os.listdir(folder)
        print("### Listing files for the Directory ### " + folder)
        print(files)
    except FileNotFoundError:
        print("Enter a valid folder name " + folder)
        continue
