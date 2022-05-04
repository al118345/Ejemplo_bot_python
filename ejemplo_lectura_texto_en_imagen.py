# -*- coding: utf-8 -*-
try:
    from PIL import Image
except ImportError:
    import Image
from PIL import ImageGrab
import pytesseract


#Leemos la imagen dónde contiene el texto.
imagen = Image.open('img/Captura.jpeg')
#transformas en español.
ocr_result = pytesseract.image_to_string(imagen, lang='spa')
print(ocr_result)



#código para obtener el texto de una parte de la pantalla.
crop_rectangle = (1000, 150, 1635, 275)
cropped_im = ImageGrab.grab(crop_rectangle)
#transformas en español.
ocr_result = pytesseract.image_to_string(cropped_im, lang='spa')
print(ocr_result)

print(ocr_result)

