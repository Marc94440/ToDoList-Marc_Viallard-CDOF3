import os
 

def AddToList(list):
    task=""
    while(task!="stop"):   
        task=input("Enter a task:")
        if(task=="stop"):
            # Clearing the Screen
            os.system('cls')
        else:
            print(task,"has been added\npress stop to exit")
            list.append(task)

def DisplayTasks(list):
    count = 1
    for element in list:
        print(count,". ",element)
        count+=1

def SaveTasks(list):
    with open('save.txt', 'w') as f:
        for element in list:
            f.write(element+"\n")

if __name__ == "__main__":
    list=[]
    AddToList(list)
    DisplayTasks(list)
    SaveTasks(list)

