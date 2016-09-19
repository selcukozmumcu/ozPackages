import os
import re
import shutil

#
## @brief Copies the file content and pastes it in the same directory by renaming
#         the file number as incremented by one. 
#
#  @param fileAbsolutePath [ str | None | in  ] - An absolute path to local file.
#  
#  @exception IOError - If the file does not exist.
#  
#  @retval None - None.
def copyAsVersion(fileAbsolutePath):
     
     
     try:
          # Checking if the file exists.
          os.path.isfile(fileAbsolutePath) == True
     
          # Extracting file Path
          filePath = os.path.dirname(fileAbsolutePath)
     
          # Extracting file name
          fileName = os.path.basename(fileAbsolutePath) 
     
          # Regex Strings to search.
          regexPath     = '/home/selcuk/Desktop/pg/textFiles/character_V(.*?).txt'
          regexFileName = 'character_V(.*?).txt'
          
          # Creating the list of file numbers.
          dirContent   = os.listdir(filePath)
          dirContentNo = []
     
          for i in dirContent:
               data   = re.findall(regexFileName, i)
               number ='{0:04}'.format(int(data[0]))
               dirContentNo.append(number)
     
          # Extracting the file number as list item
          numberStr = re.findall(regexPath, fileAbsolutePath)
          
          # Converting list item into a four digit integer
          number = '{0:04}'.format(int(numberStr[0]))
          
          # Part-1: fileNo + 1 is the default first step.     
          fileNo = '{0:04}'.format(int(number)+1)
          
          # Part-2: If the file does not exist in the current folder.
          #         It is saved as is.
          while fileNo not in dirContentNo: 
          
               # Updating the fileName with the new fileNo
               fileName = fileName.replace(fileName[-8:-4],str(fileNo))
               fileAbsolutePath2 = os.path.join(filePath,fileName)
               
               # Copying the file to destination directory
               shutil.copyfile(fileAbsolutePath, fileAbsolutePath2)
               
          # Part-3: If the file exists in the dirContentNo.
          else:
               # Increments the fileNo by one, then checks if it exists in dirContentNo.
               while fileNo in dirContentNo:
               
                    # Incrementing the fileNo by one.
                    fileNo = '{0:04}'.format(int(fileNo)+1)
                    
               # if the incremented fileNo does not exist in dirContentNo, 
               # then pastes the fileContent into the new file and saves it.
               else:
                    # Updating the fileName with the incremented fileNo.
                    fileName = fileName.replace(fileName[-8:-4],str(fileNo))
                    fileAbsolutePath2 = os.path.join(filePath,fileName)
                    
                    # Copying the file to destination directory.
                    shutil.copyfile(fileAbsolutePath, fileAbsolutePath2)
     except:
          raise IOError ('File does not exist!')

if __name__ == '__main__':
     copyAsVersion(fileAbsolutePath='/home/selcuk/Desktop/pg/textFiles/character_V0004.txt')