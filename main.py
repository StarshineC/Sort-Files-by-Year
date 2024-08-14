
def main():
    paths = open("input.txt")
    outDir = paths.readline()[:-1]
    inDir  = paths.readlines()
    paths.close()


    for directory in inDir:
        # I need \n gone
        dir = directory[:-1]

        # No Directory?
        if not os.path.exists(dir):
            stdio.writeln(f'| "{dir}" does not exist...')
            continue
        
        # List of files in directory
        files = os.listdir(dir)

        # No Files?
        if len(files) == 0:
            stdio.writeln(f'| No files in "{dir}"')
            continue

        # Yes Files?
        stdio.writeln(f'| Sorting "{dir}"...')
        for file in files:
            path = f'{dir}/{file}'
            
            # Is Directory?
            if not os.path.isfile(path):
                if not os.path.exists(f'{outDir}/other'): os.makedirs(f'{outDir}/other')
                os.rename(path, f'{outDir}/other/{file}')
                stdio.writeln(f'|| Moved {file} (other)')
            # Other Files
            else:
                # Get Year
                createdTime = os.path.getctime(path)
                createdYear = int(time.ctime(createdTime)[-4:])
                # Move to a Folder
                if not os.path.exists(f'{outDir}/{createdYear}'): os.makedirs(f'{outDir}/{createdYear}')
                os.rename(path, f'{outDir}/{createdYear}/{file}')
                stdio.writeln(f'|| Moved {file} ({createdYear})')
    
    stdio.writeln("Done!")
    return

    """
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
    """

    stdio.writeln("-=-=-= Completed Sorting! =-=-=-")
    return


if __name__ == "__main__":
    import stdio
    import os
    import time
    
    main();