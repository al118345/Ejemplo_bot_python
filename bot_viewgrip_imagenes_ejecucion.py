# -*- coding: utf-8 -*-
from pynput.mouse import Button, Controller
import time

from screen_search import Search

mouse = Controller()
def click_raton_posicion (x,y):
    mouse.position = (x, y)
    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(1)



def imagen():
    search = Search("img/viewgrip_start.png")
    pos = search.imagesearch()
    print('dasda')
    if pos[0] == -1:
        return False
    else:
        return pos

print('dasda')
while True:
    coordenadas = imagen()
    if coordenadas!= False:
        click_raton_posicion (coordenadas[0], coordenadas[1])
    time.sleep(150)

'''
while True:
    time.sleep(3)
    click_raton_posicion(1292.8883056640625, 624.0977783203125)
    click_raton_posicion(1285.159423828125, 725.6664428710938)
    click_raton_posicion(1285.74755859375, 835.3446655273438)
    click_raton_posicion(82.78189086914062, 60.03361511230469)
    time.sleep(5000)
'''