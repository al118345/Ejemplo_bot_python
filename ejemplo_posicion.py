
from pynput.mouse import Listener


def on_click(x, y, button, pressed):
    print('({0},{1})    '.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False



cont = 0
while cont < 4:
    cont = cont +1
    # evento para captar la posicion del click
    with Listener(
            on_click=on_click,
    ) as listener:
        listener.join()


