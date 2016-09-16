import re
import urllib2

#
## @brief Scans images at the given URL with a given regexString and
#         returns a list of images in the URL.
#
#  @param matchStr [ string | None | in  ] - Regex string to find targeted items in the given URL.
#  @param imageURL [ string | None | in  ] - Destination URL to search images in.
#  
#  @exception N/A
#  
#  @retval None - None.
def imageScan(matchStr, imageURL):
       
       # Checking if the link exists or not!
       try:
              # Opening and reading the imageURL
              html        = urllib2.urlopen(imageURL)
       except urllib2.HTTPError, e:
              print(e.code)           

       # Reading the URL content
       htmlContent = html.read()
       
       # Finding matches according to regex string
       matches = re.findall(matchStr, htmlContent, re.DOTALL)
       
       # Removes the '/' at the beginning of the string to prepare it for 'os.path.join' function.
       return [x[1:] for x in matches]

if __name__=='__main__':
    
       imageScan(matchStr, imageURL)