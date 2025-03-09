import os

listFile = "tasks.txt"

def main():
    createFile()

    while True:
        choice = int(input("\n------Menu------\n1. View List\n2. Add to List\n3. Remove From List\n4. Delete List\n5. Quit\n\n"))
        while choice < 1 or choice > 5:
            choice = int(input("\nInvalid Choice\n\n"))

        toDoList = readList()

        if choice == 1:
            print("\n------To-Do List:------\n")
            for item in toDoList:
                print(item)
            #print("\n\n")
        elif choice == 2:
            newTask = input("------What task would you like to add to your list?------\n\n")
            addToList(newTask)
        elif choice == 3:
            removeFromList(toDoList)
        elif choice == 4:
            deleteCheck()
        else:
            print("\nGoodbye!")
            break

#create tasks.txt
def createFile():
    if not (os.path.exists(listFile)):
        with open(listFile, "x") as f:
            pass

#return whole list
def readList():
    with open(listFile) as file:
        toDoList = [line.rstrip() for line in file]
    return toDoList

#add to the list
def addToList(newTask):
        with open(listFile, "a") as f:
            f.write(newTask + "\n")

#makes sure user wants to delete
def deleteCheck():
    choice = input("\n------Are you sure you want to delete the To-Do List? (y/n)------")
    while choice != "y" and choice != "n":
        choice = input("\nInvalid Choice\n\n")
    if choice == "y":
        open(listFile, 'w').close()

#remove an item from the list
def removeFromList(toDoList):
    print("\n------Delete------")
    for item in toDoList:
        print(str(toDoList.index(item) + 1) + ". " + item)

    choice = int(input("\nWhich task would you like to delete\n"))
    
    while choice < 1 or choice > len(toDoList):
        choice = int(input("\nInvalid Choice\n\n"))
    with open(listFile, "r") as f:
        lines = f.readlines()
    with open(listFile, "w") as f:
        for line in lines:
            if line.strip("\n") != toDoList[choice-1]:
                f.write(line)   

main()