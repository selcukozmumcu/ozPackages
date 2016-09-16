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
#  @exception IOError   - If the filePath cannot be created, then raises IOError: 
#                         "filePath does not exist!Please check the path."
#  
#  @exception HTTPError - If the given imageURL is wrong or does not exist, then returns None. 

#  @retval None - None.
def downloadImage(imageURL, filePath): 
    
    try:
        # Checking if the given path exists or not.
        if not os.path.exists(filePath) and os.path.isdir(filePath):
            
            # Creates the filePath if does not exist.
            os.makedirs(filePath)
    except:    
        raise IOError('\nfilePath does not exist!\nPlease check the path.\n')      


    # Checking if the link exists or not!
    try:
        # Opening and reading the imageURL
        fileContent = urllib2.urlopen(imageURL)
   
    except urllib2.HTTPError, e:
        return None        

    
    else:    
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

