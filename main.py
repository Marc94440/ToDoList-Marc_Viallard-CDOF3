import os
 

def AddToList(list):
    os.system('cls')
    task=""
    while(task!="stop"):   
        task=input("Enter a task:")
        if(task=="stop"):
            # Clearing the Screen
            os.system('cls')
        else:
            print(task,"has been added\nwrite stop to exit")
            list.append([task,"False"])

def DeleteTask(list):
    Tasks_delete_display(list)
    number = input("Which task do you want to delete: ")
    try:
        number = int(number)
        if 1 <= number <= len(list):
            list.pop(number - 1)
            print("The task has been deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    
    exit = input("Type anything to exit")

def CompleteTask(list):
    DisplayTasks(list)
    completenumber=input("Which task do you want to complete : ")
    for element in range(len(list)):
        if(int(completenumber)< len(list)):
            print("The task number :",completenumber,"will be completed")
            list[int(completenumber-1)][1]="True"
    print("TODO")


def Tasks_delete_display(list):
    os.system('cls')
    count = 1
    for element in list:
        if(element[1]=="False"):
            print("[]"+str(count)+". ",element[0]+"\n")
        else:
            print("[X]"+str(count)+". ",element[0]+"\n")
        count+=1


def DisplayTasks(list):
    os.system('cls')
    count = 1
    for element in list:
        if(element[1]=="False"):
            print("[]"+str(count)+". ",element[0]+"\n")
        else:
            print("[X]"+str(count)+". ",element[0]+"\n")
        count+=1
    exit=input("Type anything to exit")

def SaveTasks(list):
    with open('save.txt', 'w') as f:
        for element in list:
            f.write(element[0]+";"+element[1]+"\n")

def OpenSave(list):
    if(os.path.isfile("save.txt")):
        print("A List has been loaded")
        with open('save.txt', 'r') as f:
            for lines in f:
                lines=lines.replace("\n","")
                lines = lines.split(";")
                list.append([lines[0],lines[1]])
    else:
        print("No list found, let's create a new one\n")

def Menu(list):
    os.system('cls')
    print(10*"-"+"     Welcome to the to do list app     "+10*"-"+"\n")
    OpenSave(list)
    print("Add a task to the to do list : Type 1\n")
    print("Delete a task in the to do list : Type 2\n")
    print("Complete a task in the to do list : Type 3\n")
    print("See all tasks in the to do list : Type 4\n")
    print("Quit : Type 5\n")
    answer=input("What do you want to do ?")
    match answer:
        case "1":
            AddToList(list)
            Menu(list)

        case "2":
            DeleteTask(list)
            Menu(list)

        case "3":
            CompleteTask(list)
            Menu(list)
        
        case "4":
            DisplayTasks(list)
            Menu(list)

        case "5":
            print("Goodbye")

        case _:
            print("The input is incorrect")
            exit=input("Type anything to exit")
            Menu(list)

if __name__ == "__main__":
    os.system('cls')
    list=[]
    Menu(list)
    SaveTasks(list)

