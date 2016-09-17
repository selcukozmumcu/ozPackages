import os


def copyAsVersion(fileAbsolutePath):
     
     # Defining and Separating all needed parameters
     fApSplit = os.path.split(fileAbsolutePath)
     filePath = fApSplit[0]
     fileName = os.path.basename(fileAbsolutePath)
     
     # Listing the file numbers of the current content in the folder.
     dirContent   = os.listdir(filePath)
     dirContentNo = []
     for i in dirContent:
          dirContentNo.append(int(i[-5]))
     
     # Part-1: fileNo + 1 is the default first step.     
     fileNo   = int(fileName[-5])+1     
     
     # Part-2: If the file does not exist in the current folder.
     #         It is saved as is.
     if not fileNo in dirContentNo:
          
          # Updating the fileName with the new fileNo
          fileAbsolutePath = fileAbsolutePath.replace(fileAbsolutePath[-5], str(fileNo))
          with open(fileAbsolutePath, 'w') as fob:
               fob.write(' ')
          
     # Part-3: If the file exists in the dirContentNo.   
     else:          
          while fileNo in dirContentNo:
               
               fileNo +=1
          
          else:
               # Updating the fileName with the new fileNo
               fileAbsolutePath = fileAbsolutePath.replace(fileAbsolutePath[-5], str(fileNo))
               with open(fileAbsolutePath, 'w') as fob:
                    fob.write(' ')
     

if __name__ == '__main__':
     copyAsVersion(fileAbsolutePath='/home/selcuk/Desktop/pg/textFiles/character_V002.txt')