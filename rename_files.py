import os

def rename_files():
    #(1) get file names froma folder
    file_list = os.listdir(r"C:\Crank\03-11-15, Data Science + Computer Science + Python, (Learn+Practice+Immerse+Evolve, Core Skillset)\1, Udacity - Programming Foundations with Python\Exercises, Assignments and Projects\1.2 Secret Message\prank")
    print(file_list)
    #(2) for each file, rename filename
    saved_path = os.getcwd()
    os.chdir(r"C:\Crank\03-11-15, Data Science + Computer Science + Python, (Learn+Practice+Immerse+Evolve, Core Skillset)\1, Udacity - Programming Foundations with Python\Exercises, Assignments and Projects\1.2 Secret Message\prank")
    for file_name in file_list:
        print("Old Name - " + file_name)
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print("New Name - " + file_name)
    os.chdir(saved_path)

rename_files()
