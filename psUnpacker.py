import os

workDir = os.getcwd()

def main():
    workDirContents = os.listdir(workDir)
    for file in workDirContents:
        if not os.path.isdir(file):
            print("[SCAN]   | " + file + " -> Not a directory. Skipping.")
            continue
        print("[SCAN]   | " + file + " -> Valid directory. Moving contents.")
        moveContents(file)
    input("[FINISH] | Press any key to exit...")

def moveContents(dir):
    dir = os.chdir(dir)
    dirChildren = os.listdir(dir)
    for file in dirChildren:
        destFilePath = os.path.join(workDir, file)
        curFilePath = os.path.abspath(file)
        try:
            os.renames(curFilePath, destFilePath)
            print("[MOVED] | " + file + " -> " + workDir)
        except FileNotFoundError:
            print("[ERROR]  | " + curFilePath + " -> File does not exist. Skipping")
        except FileExistsError:
            print("[ERROR]  | " + curFilePath + " -> File already exists in destination. Skipping.")
    print("[FINISH] | " + os.getcwd())
    os.chdir("..")

main()