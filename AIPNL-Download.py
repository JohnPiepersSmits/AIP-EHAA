#
# Script to download the AIP pdf files from www.ais-netherlands.nl
#
# EH-AD ranges: 0.1 - 0.6, 1.1 - 1.5
# EH-ENR ranges: 0.1 - 0.6, 1.1 - 1.14, 2.1 - 2.2, 3.1 - 3.6, 4.1 - 4.5, 5.1 - 5.6, 6
# EH-GEN ranges: 0.1 - 0.6, 1.1 - 1.7, 2.1 - 2.7, 3.1 - 3.6, 4.1 - 4.2
#
# Note: ENR-6 Charts are not available for download at these urls
#
# Publication dates:
# old:          http://www.ais-netherlands.nl/aim/2018-11-22-AIRAC/pdf/
# current:         http://www.ais-netherlands.nl/aim/2018-12-20-AIRAC/pdf/
# next:         http://www.ais-netherlands.nl/aim/2011-01-17-AIRAC/pdf/
#


import wget
import ssl
import os
import time


downloadDir = "D:\\USBdisk\\Aviation\\eAIP-EHAA\\Download"
urlAIPnl = "http://www.ais-netherlands.nl/aim/2018-12-20-AIRAC/pdf/"


AIPNL = {
    "GEN": [
        {
            "name": "EH-GEN-",
            "totalChapters": 5,
            "pagesChapter": (7, 8, 8, 7, 3)
        }
    ],
    "ENR": [
        {
            "name": "EH-ENR-",
            "totalChapters": 6,
            "pagesChapter": (7, 15, 3, 7, 6, 7)
        }
    ],
    "AD": [
        {
            "name": "EH-AD-",
            "totalChapters": 2,
            "pagesChapter": (7, 6)
        }
    ]
}


# change to download dir
os.chdir(downloadDir)

# setup ssl for wget
ssl._create_default_https_context = ssl._create_unverified_context


def downloadPDF(PDFname):                       # download the files
    print("\nDownloading: " + PDFname)
    try:
        wget.download(urlAIPnl + PDFname)
    except:
        print("\nError downloading: " + PDFname)
    time.sleep(2)


# create the filename from the keys of each section and download it
def createPDFfilename(name, nrChapters, nrPages):
    for i in range(0, nrChapters):
        for j in range(1, nrPages[i]):
            downloadPDF(name + str(i) + "." + str(j) + ".pdf")


# scan the dictionary, get sections (GEN, ENR, AD) and their keys (name, chapters and pages)
for section in AIPNL.keys():
    for chapter in AIPNL.get(section):
        createPDFfilename(
            chapter["name"], chapter["totalChapters"], chapter["pagesChapter"])


print("\nDownload completed!")
