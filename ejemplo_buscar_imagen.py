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



def imagen(imagen):
    search = Search(imagen)
    pos = search.imagesearch()
    if pos[0] == -1:
        return False
    else:
        return pos


time.sleep(3)
path = 'img/'
coordenadas = imagen(path+ 'logo.png')
#si encuentro
if coordenadas!= False:
        click_raton_posicion (coordenadas[0], coordenadas[1])



