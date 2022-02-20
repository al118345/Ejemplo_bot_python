# -*- coding: utf-8 -*-
from pynput.mouse import Listener
#función para obtener las coordenadas del lugar de la pantalla dónde se ha pulsado
def on_click(x, y, button, pressed):
    print('({0},{1})    '.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

#bucle for para realizar la tarea durante 4 ocasiones
cont = 0
while cont < 4:
    cont = cont +1
    print( 'Click número ' + str(cont))
    # evento para captar la posicion del click
    with Listener(
            on_click=on_click,
    ) as listener:
        listener.join()


