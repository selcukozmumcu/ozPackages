import os
import time
import getpass
import imageScanLib
import downloadImageLib

#
## @brief Scans the given URL for images, then downloads them to given path and 
#         creates an HTML with downloaded images.
#  
#  @exception N/A
#  
#  @retval None - None.
def main():
    
    # Defining URL and File Path
    url      = 'http://bereketplastik.com'
    filePath = '/home/selcuk/Desktop/pg/imagesYVR/folder1'
    
    if not os.path.islink(url):
        raise IOError('URL does not exist!')
    
    if not os.path.isdir(filePath):
        raise IOError('File Path does not exist!')    
    
    else:
        # Getting images from given URL
        scannedImages = imageScanLib.imageScan(matchStr=r'<a rel="fancyGallery" title="" href="(.*?)"><img class="product_photo" src=".*?"/></a>',
                                                imageURL='{}/products/?name=CPP%20Torbalar'.format(url),
                                                display =False)
        
        # Creating the HTML content as a string
        htmlConent = '<h1>{0} - {1}</h1><br><br>'.format(getpass.getuser(), time.asctime())
        
        # Defining the Image Content as a string
        imageContent = ''
        
        # Appending to imageContent as strings with HTML image tag
        for s in scannedImages:
            absoluteURL = os.path.join(url, s)
            try:
                absoluteLocalPath = downloadImageLib.downloadImage(imageURL=absoluteURL,
                                                                    filePath=filePath)
                imageContent += '<img src="{0}" width="250"/><br><br>{1}<br><br><br>'.format(absoluteLocalPath,
                                                                                             os.path.basename(absoluteLocalPath))
            except Exception, error:
                imageContent += '<br><br><span style="color:red;">Image {0} could not be download because of: {1}</span><br><br>'.format(absoluteURL, str(error))
        
        # Adding two strings to each other
        htmlConent += imageContent
        
        # Downloading image to given absolute path
        htmlFile = open(os.path.join(filePath, 'index.html'), 'w')
        htmlFile.write(htmlConent)
        htmlFile.close()

if __name__ == '__main__':
    
    main()