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


while True:
    coordenadas = imagen()
    #si encuentro
    if coordenadas!= False:
        click_raton_posicion (coordenadas[0], coordenadas[1])
    time.sleep(150)

