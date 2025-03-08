import os

listFile = "C:/Users/liams/OneDrive/Documents/Code Projects/Python/To-Do List/tasks.txt"

def main():
    createFile()
    toDoList = readList()

    while True:
        choice = int(input("1. View List\n2. Add to List\n3. Remove From List\n4. Delete List\n5. Quit\n\n"))
        while choice < 1 or choice > 5:
            choice = int(input("\nInvalid Choice\n\n1. View List\n2. Add to List\n3. Remove From List\n4. Delete List\n\n"))

        if choice == 1:
            print("\nTo-Do List:\n")
            for item in toDoList:
                print(item)
        elif choice == 2:
            print("2")
        elif choice == 3:
            print("3")
        elif choice == 4:
            deleteCheck()
        else:
            print("\nGoodbye!")
            break

def createFile():
    if not (os.path.exists(listFile)):
        with open(listFile, "x") as f:
            pass

def readList():
    with open(listFile) as file:
        toDoList = [line.rstrip() for line in file]
    return toDoList

def deleteCheck():
    choice = input("\nAre you sure you want to delete the To-Do List? (y/n)")
    while choice != "y" and choice != "n":
        choice = input("\nInvalid Choice\n\nAre you sure you want to delete the To-Do List? (y/n)\n")
    if choice == "y":
        open(listFile, 'w').close()

main()