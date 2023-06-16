import os

my_directory = "/Users/gotham/Projects/Skillbox/python/Zagorulko-ob-22-wd"
my_extension = ".py"


def find_files(directory, extension):
    if not os.path.isdir(directory):
        raise ValueError("Директория отсутствует")

    files_and_dirs = os.listdir(directory)

    for file_or_dir in files_and_dirs:
        full_path = os.path.join(directory, file_or_dir)

        if os.path.isdir(full_path):
            find_files(full_path, extension)
        else:
            if full_path.endswith(extension):
                print(full_path)


find_files(my_directory, my_extension)
