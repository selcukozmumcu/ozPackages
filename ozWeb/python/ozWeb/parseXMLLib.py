# -*- encoding: utf-8 -*-

#!/usr/bin/python
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @file          parseXMLLib.py [ FILE ] - Parsing XML files at the given URL.
## @package ozWeb.parseXMLLib    [ FILE ] - Consists of several types of Web applications like
#                                           File Downloads, Parsing XML, Parsing HTML and a like.
#
# ----------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------
import os
import requests
from   xml.etree import ElementTree
#
#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------

#
## @brief This function downloads the XML files from a certain URL to one of the given
#         download paths, then exctracts 'ilksureadi' and 'meal' tags from each downloaded XML
#         and saves them into an HTML file at the given download path.
#  
#  @param downloadPath [ str | None | in  ] - This is the download path for XML files.
#  @param htmlPath     [ str | None | in  ] - This is the download path for HTML files.
#  
#  @exception IOError - Raises if there is a problem with given download paths.
#  
#  @retval None - None.
def main(downloadPath,htmlPath):
    
    # Checking if the given paths exist or not.
    try:
        if os.path.isdir(downloadPath) and os.path.isdir(htmlPath) == True:
            
            # Defining required path(s)
            xmlUrl = 'http://meal.risaleonline.com/getpage.php?sayfa='
            
            pageNumber  = range(0,605)
            n = 0
            
            while n<605:
                
                for i in pageNumber:
                    
                    # Defining required paths for the given number of pages
                    xmlAddress   = ''.join([xmlUrl,str(i)])
                    xmlFileNo    = ''.join([str(i),'.xml'])
                    xmlFileName  = os.path.join(downloadPath,xmlFileNo)
                    htmlFileNo   = ''.join([str(i),'.html'])
                    htmlFileName = os.path.join(htmlPath,htmlFileNo)
                
                    # -----READING the XML File-----
                    response = requests.get(xmlAddress)
                    xmlFile = response.content
                    
                    
                    # -----REPLACING TURKISH CHARACTERS TO ENGLISH-----
                    # Defining which unrecognized characters to be replaced when found
                    trLetter = {'ü':'u','û':'u', 'ı':'i', 'î':'i', 'ī':'i', 'ğ':'g', 'ş':'s', 'â':'a', 'ā':'a', 'ö':'o', 'Â':'A', 'Û':'U', 'İ':'I'}
                    
                    # Replacing the Turkish characters with the English versions
                    for t in trLetter:
                        xmlFile = xmlFile.replace(t, trLetter[t])
                    
                    # -----DOWNLOADING the XML File-----
                    with open(xmlFileName, 'w') as fob:
                        fob.write(xmlFile)
                    
                    
                    # -----CREATING AN HTML FILE-----
                    # Parsing the XML File
                    dom =  ElementTree.parse(xmlFileName)
                    
                    # Creating HTML content
                    sureName    = (dom.find('ilksureadi')).text
                    mealContent = (dom.find('meal')).text
                    
                    htmlContent = """
                    <html>
                    <head>
                    <meta charset="utf-8">
                    <title>%s-%s</title>
                    </head>
                    <body align='center'>
                    <h1>%s</h1><br>
                    %s
                    </body>
                    </html>
                    """ %(str(i),sureName, sureName, mealContent)
                    
                    # Creating the HTML File
                    with open(htmlFileName, 'w') as htmlFile:
                        htmlFile.write(htmlContent.encode('utf-8'))
                        
                    n +=1
    except:
        raise IOError('Path does not exist!\nCheck both of the paths given.')
            
if __name__ == '__main__':
    
    main(downloadPath='/home/selcuk/Desktop/pg/XML', 
         htmlPath    ='/home/selcuk/Desktop/pg/XML/HTML' )