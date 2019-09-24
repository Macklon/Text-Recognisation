from PIL import Image
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

f = open('output.txt','a')
indir = 'img/'
for root, dirs, filenames in os.walk(indir):
    for filename in filenames:
        print ('--- Start recognize text from '+ filename +' ---')
        file = Image.open(indir + filename)
        output = pytesseract.image_to_string(file, lang='eng')
        f.write(output)
        print ('------ Done -------')

f.close()
