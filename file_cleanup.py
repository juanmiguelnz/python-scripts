import os

directory = '/Users/miguelj/sample/directory'
os.chdir(directory)

for folders, subfolders, files in os.walk(directory):
    for file in files:
        if '.txt' in file:
            remove_text_file = os.path.join(folders, file)
            os.remove(remove_text_file)
        if '.mht' in file:
            remove_mht_file = os.path.join(folders, file)
            os.remove(remove_mht_file)
        if '.DS_Store' in file:
            remove_ds_file = os.path.join(folders, file)
            os.remove(remove_ds_file)

    # print('DIRECTORY', folders)
    # print('>> SUBFOLDER' ,subfolders)
    # print('>>> FILES',files)