import os

taskFile = "C:/Users/liams/OneDrive/Documents/Code Projects/Python/To-Do List/tasks.txt"

def createFile():
    if not (os.path.exists(taskFile)):
        with open(taskFile, "x") as f:
            pass

def main():
    createFile()

main()