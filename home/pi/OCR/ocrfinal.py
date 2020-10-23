import os
import subprocess


p = subprocess.Popen(["tesseract", "--tessdata-dir", "/usr/share/tesseract-ocr", "trytess.jpg", "zorotext", "-l", "eng", "-psm", "3"], stdout=subprocess.PIPE)
output, err = p.communicate()
print output


