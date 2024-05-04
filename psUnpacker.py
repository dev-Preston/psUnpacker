import os
workDir = os.getcwd()

def main():
    promptConfirm()
    for file in os.listdir(workDir):
        if not os.path.isdir(file):
            print("[SCAN]   | " + file + " -> Not a directory. Skipping.")
            continue
        print("[SCAN]   | " + file + " -> Valid directory. Moving contents.")
        moveContents(file)
    input("[FINISH] | Press any key to exit...")

def promptConfirm():
    confirm = input("Are you sure you want to run psUnpacker in this directory? y/n\n")
    if (confirm != "n") and (confirm != "y"):
        promptConfirm()
    elif confirm == "n":
        exit()

def moveContents(dir):
    os.chdir(dir)
    dir = os.getcwd()

    dirChildren = os.listdir(dir)

    for file in dirChildren:
        curFilePath = os.path.abspath(file)
        destFilePath = os.path.join(workDir, file)
        try:
            os.renames(curFilePath, destFilePath)
            print("[MOVED]  | " + file + " -> " + workDir)
        except FileNotFoundError:
            print("[ERROR]  | " + curFilePath + " -> File does not exist. Skipping")
        except FileExistsError:
            print("[ERROR]  | " + curFilePath + " -> File already exists in destination. Skipping.")

    os.chdir("..")
    os.rmdir(dir)
    print("[FINISH] | " + dir)
        

main()