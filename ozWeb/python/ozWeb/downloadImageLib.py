# -*- encoding: utf-8 -*-

import urllib2
import os

#
## @brief Downloads a single image by the given imageURL to destination path,
#         returns the absolute path of the downloaded image.
#  
#  @param imageURL [ str | None | in  ] - Absolute path for image URL.
#  @param filePath [ str | None | in  ] - Absolute path for download destination.
#  
#  @exception N/A
#  
#  @retval None - None.
def downloadImage(imageURL, filePath):
    
    # Checking if the URL exists and valid.
    if not os.path.isfile(imageURL):
        raise IOError('\nImage URL does not exist!\nPlease check the URL address.\n')    
    
    # Checking if the given path exists or not.
    if not os.path.exists(filePath) and os.path.isdir(filePath):
        raise IOError('\nFile path does not exist!\nPlease check the path.\n')      
    
    else:    
        # Opening the imageURL
        fileContent = urllib2.urlopen(imageURL)
        
        # Defining which unrecognized characters to be replaced when found
        trLetter = {'ü':'u', 'ı':'i', 'ğ':'g', 'ş':'s', ' ':''}
        
        # Extracting the file name from the image URL
        baseName = os.path.basename(imageURL)
        
        # Replacing the Turkish characters with the English versions
        for i in trLetter:
            baseName = baseName.replace(i, trLetter[i])
        
        # Creating an absolute path with the updated file name    
        # Right way to append to a path or create an absolute path
        absolutePath = os.path.join(filePath, baseName)
        
        # Downloading the image to the updated absolute path
        output = open(absolutePath,'wb')
        data = output.write(fileContent.read())
        output.close()
    
    # Returns the downloaded file's absolute path with the name.
    return absolutePath

if __name__=='__main__':
    
    downloadImage(imageURL, filePath)
