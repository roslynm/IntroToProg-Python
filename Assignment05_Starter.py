# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):# RRoot,1.1.2030,Created started script
# Roslyn Melookaran,5/14/20,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# Declare variables and constants
strFile = "ToDoList.txt"   # File Name
lstData = ""  # A row of text data from the file, ** Note, I changed this from the initial "strData" because I am reading in a row from file as a list and not a string
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
ObjFile= None # Object that represents the file
# Add information into the .txt file
objFile=open(strFile, "w")
dicRow = {"Task":"Laundry","Priority": "High"}
objFile.write(dicRow["Task"]+ ',' + dicRow["Priority"] + '\n')
dicRow = {"Task":"Dishes","Priority": "Low"}
objFile.write(dicRow["Task"]+ ',' + dicRow["Priority"] + '\n')
dicRow = {"Task":"Homework","Priority": "Medium"}
objFile.write(dicRow["Task"]+ ',' + dicRow["Priority"] + '\n')
objFile.close()
# Define menu of user options
strMenu = """    
    Menu of Options    
    1) Show current data    
    2) Add a new item.    
    3) Remove an existing item.    
    4) Save Data to File    
    5) Exit Program    """

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile=open(strFile, "r")
for row in objFile:
    lstData = row.split(",")  # Returns row as a list
    dicRow = {"Task": lstData[0].strip(), "Priority": lstData[1].strip()}  # Note strip function to get rid of extra spaces and carraige return
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print("Task- "+row.get("Task")+", Priority- "+row.get("Priority"))
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask=input("Please enter a task: ")
        strPriority=input("Please enter a priority: ")
        dicRow={"Task":strTask,"Priority":strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        removeChoice=input("Please type in the task you would like to remove: ")
        for i in range(len(lstTable)):
            if lstTable[i]['Task'] == removeChoice:
                print("Task: " + lstTable[i]["Task"] +", Priority: " + lstTable[i]["Priority"]+", has been removed")
                del lstTable[i]
                break
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        print("Your tasks have been written to the file!")
        for row in lstTable:
            objFile.write(row.get("Task") + ", " + row.get("Priority")+"\n")
        objFile.close()
        continue


    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Thanks for using this program!")
        break  # and Exit the program