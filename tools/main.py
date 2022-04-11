import os

def validate():
    if os.path.exists("../folder1"):
        print("folder1 exists")
    else: 
        print("folder1 doesnt exist")

validate()