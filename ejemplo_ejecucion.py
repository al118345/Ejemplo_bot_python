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
    time.sleep(10)


git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/al118345/Ejemplo_bot_python.git
git push -u origin main

click_raton_posicion(626.6600341796875, 181.1196746826172)