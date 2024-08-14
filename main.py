
def main():
    inDir  = input("> Input Directory: ")
    outDir = input("> Output Directory: ")

    # Get file list
    files = os.listdir(inDir)

    # No Files
    if len(files) == 0 :
        stdio.writeln("-=-=-= No files to Sort! =-=-=-")
        return
    
    # Yes Files
    for file in files:
        # Get Year
        path = f'{inDir}/{file}'
        createdTime = os.path.getctime(path)
        createdYear = int(time.ctime(createdTime)[-4:])
        # Move to a Folder
        if not os.path.exists(f'{outDir}/{createdYear}'): os.makedirs(f'{outDir}/{createdYear}')
        os.rename(path, f'{outDir}/{createdYear}/{file}')
        stdio.writeln(f'Moved {path} to {outDir}/{createdYear}/{file}')


    stdio.writeln("-=-=-= Completed Sorting! =-=-=-")
    return


if __name__ == "__main__":
    import stdio
    import os
    import time
    
    main();