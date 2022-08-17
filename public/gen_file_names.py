import os

directory = os.fsencode('monstersv1')

print('type,url')
for file1 in os.listdir(directory):
    dir_name = os.fsdecode(file1)
    for file2 in os.listdir(f'monstersv1/{dir_name}'):
        file_name = os.fsdecode(file2)
        if "AirDrop" not in file_name or "AirDrop" in dir_name:
            print(f'{dir_name},https://test.bcmhunt.com/assets/monstersv1/{dir_name}/{file_name}')
