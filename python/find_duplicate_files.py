import hashlib
import os
def get_files(given_directory):
    duplicate_file_dict = {}
    for files in os.listdir(given_directory):
        hasher = hashlib.md5()
        filePath = os.path.join(given_directory,files)
        if os.path.isdir(filePath):
            get_files(filePath)
        else:
            with open(filePath, 'rb') as aFile:
                buffer = aFile.read()
                hasher.update(buffer)
                duplicate_file_dict.setdefault(hasher.hexdigest(),[]).append(filePath)
    for key in duplicate_file_dict:
        list_of_files = duplicate_file_dict[key]
        if len(list_of_files) > 1:
            print(duplicate_file_dict[key])



get_files("/tmp/python")
