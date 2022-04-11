import os

def validate():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    print(os.listdir(dir_path))
    print(os.listdir(os.path.join(dir_path,os.pardir)))
    if os.path.exists("../folder1"):
        print("folder1 exists")
    else: 
        print("folder1 doesnt exist")

validate()