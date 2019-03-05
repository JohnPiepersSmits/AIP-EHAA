#
# Script to download the AIP AERODROME(AD) pdf files from www.ais-netherlands.nl
#
# EH-AD Aerodromes: EH-AD-2.EHXX
#
# Publication dates:
# old:          http://www.ais-netherlands.nl/aim/2018-11-22-AIRAC/pdf/
# current:         http://www.ais-netherlands.nl/aim/2018-12-20-AIRAC/pdf/
# next:         http://www.ais-netherlands.nl/aim/2019-01-17-AIRAC/pdf/
#


import wget
import ssl
import os
import time

aipADaerodromes = ["EHAL", "EHAM", "EHBD", "EHBK", "EHDR", "EHEH", "EHGG", "EHHO", "EHHV", "EHKD",
                   "EHLE", "EHMZ", "EHOW", "EHRD", "EHSE", "EHST", "EHTE", "EHTL", "EHTW", "EHTX"]


downloadDir = "D:\\USBdisk\\Aviation\\eAIP-EHAA\\Download"
urlAIPnl = "http://www.ais-netherlands.nl/aim/2018-12-20-AIRAC/pdf/"


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


# Now get the aerodrome files
for loop in aipADaerodromes:
    downloadPDF("EH-AD-2." + loop + ".pdf")

print("\nDownload completed!")
