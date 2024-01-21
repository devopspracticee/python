import os

file_path = "prathap.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print(f'The file {file_path} is deleted')
else:
    print(f'The file {file_path} does not exixts')
