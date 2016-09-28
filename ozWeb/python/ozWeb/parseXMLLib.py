#!/usr/bin/python
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @file    [u'parseXMLLib'].py [ FILE ] - Downloading XML files, extracts required content and 
#                                             saves it as an HTML file..
## @package parseXMLLib         [ FILE ] - Downloading XML files, extracts required content and 
#                                             saves it as an HTML file..


#
# ----------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------
import os
import re
import requests
import xml.etree.ElementTree as ET
#
#-----------------------------------------------------------------------------------------------------
# CODE
#----------------------------------------------------------------------------------------------------
#
## @brief Downloading XML files, extracts required content and saves it as an HTML file.
#  
#  @param destinationDir [ str | None | in  ] - Destination Directory for HTML files.
#  
#  @exception IOError - Raises when destination directory does not exist.
#
#  @exception N/A - Raises when internet connection related errors occur.
#
#  @retval None - None.
def main(destinationDir):
    
    # Creating HTML Code
    htmlHead = u"""
    <html>
    <head>
    <title>%s-%s</title>
    <meta charset="utf-8">
    <style>
    .section{
    font-size:18px;
    font-family:arial;
    font-weight:bold;
    }
    </style>
    </head>
    """
    htmlBody = u"""
    <body style="background:lightgrey">
    <h1>{0}</h1>
    <div class="section">
    <p>{1}</p>
    </div>
    </body>
    </html>
    """
    
    
    
    
    # Source URL defined
    url = 'http://meal.risaleonline.com/getpage.php?sayfa=%d'
    
    # Creating the loop for 605 pages
    for i in range(0,605):
        
        # Creating the working URL with page number at the end
        xmlURL = url %i
        
        # Checking the given URL
        try:
            response = requests.get(xmlURL)
        except requests.exceptions.RequestException as e:
            print e
        else:
            # Reading the URL content
            xmlFile  = response.content

        
            # Unrecognized characters defined, then being converted to UTF-8 when found
            trLetter = {'ü':'u','û':'u', 'ı':'i', 'î':'i', 'ī':'i', 'ğ':'g', 'ş':'s', 'â':'a', 'ā':'a', 'ö':'o', 
                        'Â':'A', 'Û':'U', 'İ':'I', 'Ö':'O', 'ç':'c', 'Ş':'S', 'Ç':'C', 'Ü':'U', 'Ğ':'G', '‘':'-', '’':'-'}
            for x in trLetter:
                xmlFile = xmlFile.replace(x, trLetter[x])
            
            
            # There is an extra tag within the first page so handling it here to make it egual with the rest.
            if i == 0:
                noSureBaslik   = re.sub('<span class=.*?>.*?</span><sup>.*?</sup>','', xmlFile)
                # Removing image tags from the whole XML file
                noImageXMLFile = re.sub('<img .*?>','', noSureBaslik)
            else:
                noSureBaslik   = re.sub('<span class=.*?>.*?</span><.../>','', xmlFile)
                # Removing image tags from the whole XML file
                noImageXMLFile = re.sub('<img .*?>','', noSureBaslik)
            
            
            # Checking the XML file, then parsing it
            try:
                xmlRead  = ET.fromstring(noImageXMLFile) 
            except Exception.error:
                print error
            else:
                # Extracting required tags from the XML file
                sureName = xmlRead.find('ilksureadi').text
                content  = xmlRead.find('meal').text
                
                # Formating the HTML content parts and unifies them as htmlContent.
                htmlHeadContent = htmlHead %(str(i), sureName)
                htmlBodyContent = htmlBody.format(sureName, content)
                htmlContent     = u'{0}{1}'.format(htmlHeadContent,htmlBodyContent)
                
                # Creating the HTML File
                with open('{0}/{1}-{2}.html'.format(destinationDir, '{0:03}'.format(i), sureName), 'w') as htmlFile:
                    htmlFile.write(htmlContent.encode('utf-8'))


if __name__ == '__main__':
    main(destinationDir = '/home/selcuk/Desktop/pg/HTML')