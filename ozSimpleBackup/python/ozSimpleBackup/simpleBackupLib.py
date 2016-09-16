import os
import re
import shutil
import datetime
import soCore.fileSystemLib

#
## @brief Backing up a local folder to another one with the exact time embedded in backup directory name.
#  
#  @param sourceDir      [ str  | None  | in  ] - Source directory as absolute path.
#  @param destinationDir [ str  | None  | in  ] - Destination directory as absolute path.
#  @param display        [ bool | False | in  ] - Optional argument: Displays the absolute path of the copied content.
#  
#  @exception IOError -  When something wrong with the Source Directory.
#
#  @exception IOError -  When Destination Directory cannot be created.
#
#
#  @retval None - None.
def simpleBackup(sourceDir, destinationDir, display=False):
    
    # Checking if the given directory exists or not!
    if not os.path.isdir(sourceDir):
        raise IOError('\nSomething wrong with the Source Directory.\nPlease check the given path!\n')
    
    try:
        # Checking if the given directory exists or not!
        if not os.path.isdir(destinationDir):

            # Creates the non-existent destination directory.
            os.makedirs(destinationDir)    
    
    except:    
        raise IOError('\nSomething wrong with the Destionation Directory.\nPlease check the given path!\n')    
    
    # Create a new Directory  with a name, time and date embedded 
    # at the Destination Directory 
    localTime     = datetime.datetime.strftime(datetime.datetime.now(), '{1}{0}%Y.%m.%d{1}{2}%H.%M.%S'.format('D','_','T'))
    directoryName = ''.join([os.path.basename(sourceDir),localTime])
    
    destinationAbsolutePath = os.path.join(destinationDir,directoryName)
        
    # Copy all Source Directory content into the New Destination Directory
    shutil.copytree(sourceDir, destinationAbsolutePath)
       
    # Prints the Destination Directory content with their absolute paths
    if display:
        destinationContent = soCore.fileSystemLib.Directory(directory=destinationAbsolutePath)
        for i in destinationContent.listFilesRecursively(extension=''):
            print i
