import os

if not os.path.exists('./my_folder'):
    os.makedirs('my_folder')
else:
    print("Директория уже существует")
