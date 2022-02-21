# -*- coding: utf-8 -*-
from pynput.mouse import Button, Controller
import time
mouse = Controller()
def click_raton_posicion (x,y):
    mouse.position = (x, y)
    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(1)
while True:
    time.sleep(3)
    click_raton_posicion(1292.8883056640625, 624.0977783203125)
    click_raton_posicion(1285.159423828125, 725.6664428710938)
    click_raton_posicion(1285.74755859375, 835.3446655273438)
    click_raton_posicion(82.78189086914062, 60.03361511230469)
    time.sleep(5000)