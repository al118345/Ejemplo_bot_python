# -*- coding: utf-8 -*-

try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract



#Leemos la imagen dónde contiene el texto.
imagen = Image.open('img/Captura.jpeg')
#transformas en español.
ocr_result = pytesseract.image_to_string(imagen, lang='spa')
print(ocr_result)