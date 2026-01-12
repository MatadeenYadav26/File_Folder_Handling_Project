from pathlib import Path
import shutil

def create_folder():
    try:
        name = input("Tell your folder name:- ")
        p = Path(name)
        p.mkdir()
        print("Folder created successfully")
    except Exception as err:
        print("Sorry an error , occured as {err}")


def read_file_folder():
    p = Path("")
    items = list(p.rglob('*'))
    for i , v in enumerate (items):
        print(f"{i + 1} : {v}")

def update_folder():
    try:
        read_file_folder()
        old_name = input("Tell the name of folder , you want to update:- ")
        p = Path(old_name)
        if p.exists() and p.is_dir() :
            new_name = input("Please tell your new folder name :- ")
            new_p = Path(new_name)
            p.rename(new_p)
            print("Your folder name is updated successfully.")
        else:
            print("Sorry , no such folder exist.")
    except Exception as err:
        print(f"An error occured as {err}") 

def delete_folder():
    try:
        read_file_folder()
        name = input("Please , Tell the Folder You want to delete :- ")
        p = Path(name)
        if p.exists() and p.is_dir():
            shutil.rmtree(p)
            print("Folder Deleted Successfully!")
        else:
            print("No , Such Folder exists.")
    except Exception as err:
        print(f"An error occured as {err}.")

def create_file():
    try: 
        read_file_folder()
        name = input("Please tell your file name: ")
        p = Path(name)
        if not p.exists():
            with open(name,'w') as fs:
                data = input("Write , what you want in this file :- ")
                fs.write(data)
            print("File created Succesfully.") 
        else:
            print("Sorry , this name file already exisits.")    
    except Exception as err:
        print(f"An error occured as {err}.")

def read_file():
    try:
        read_file_folder()
        name = input("Tell your file name :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(name,'r') as fs:
                content = fs.read()
                print("Your file content is: ")
                print(content)
        else:
            print("Sorry , no such file exist.")
    except Exception as err:
        print(f"An error occured as {err}.")

def update_file() :
    
    try:
        read_file_folder()
        name = input("Tell your file name :- ")
        p = Path(name)
        if p.exists() and p.is_file() : 
            print("Options :- ")
            print("1. For renaming the file.")
            print("2. For appending the content in file.")
            print("3. For over-writing the file.")
            choice = int(input("Tell your choice :- "))

        if choice == 1:
            new_name = input("Tell your new name with extension :- ")
            new_p = Path(new_name)
            if not new_p.exists():
                p.rename(new_p)
                print("Your file name is changed succesfully.")
            else:
                print("Sorry, this name already exists.")
            
        if choice == 2:
            with open(name,'a') as fs:
                data = input("What you want to append : ")
                fs.write(" " + data)
            print("Data appended successfully.")

        if choice == 3:
            with open(name,'w') as fs:
                data = input("What you want to over-write : ")
                fs.write(data)
            print("Data changed successfully.")
    except Exception as err:
        print(f"An error ocurred as {err}.")

def delete_file():
    try: 
        read_file_folder()
        name = input("Tell your file name with extension: ")
        p = Path(name)
        if p.exists and p.is_file():
            p.unlink()
            print("file Deleted Successfully!")
        else:
            print("Sorry , no such file exist.")
    except Exception as err:
        print(f"An error occurred as {err}.")
        
while True:
    print("Options:- ")

    print("1. Create a folder.")
    print("2. Read files and folder.")
    print("3. Update the folder.")
    print("4. Delete the folder.")
    print("5. Create a file.")
    print("6. Read a file.")
    print("7. Update a file.")
    print("8. Delete a file.")
    print("0. Exit the program.")

    choice = int(input("please choose your option:- "))

    if choice == 1 :
        create_folder()

    elif choice == 2 :
        read_file_folder()

    elif choice == 3 :
        update_folder()

    elif choice == 4:
        delete_folder()

    elif choice == 5:
        create_file()

    elif choice == 6:
        read_file()

    elif choice == 7:
        update_file()

    elif choice == 8:
        delete_file()

    elif choice == 0:
       print("Exiting program... 👋")
       break

    else:
        print("Invalid choice! Please try again.")