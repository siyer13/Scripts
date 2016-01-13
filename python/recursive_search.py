import os

def search(file_path):
    with open(file_path) as f:
        for line in f:
            if 'data' in line and 'null' in line:
                print(file_path,line)

for root, dirs, files in os.walk('C:\\Users\\CoreJava'):
    for name in files:
        if name.endswith((".java")):
            search(os.path.join(root,name))


    
