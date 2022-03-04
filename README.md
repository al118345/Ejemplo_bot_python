# Bot en Python3 para principiantes, como conseguir que tu ordenador trabaje sólo.

## Introducción

Este tutorial consiste en la creación de un script para la automatización de tareas a través de clicks o para la lectura/pulsado de teclado en caso de necesidad.

El código esta explicado en la url https://1938.com.es/bot-click-python

### Files

En este repositorio se pueden encontrar los siguientes ficheros:

* **ejemplo_ejecucion_bot_click.py**  Ejemplo de bot click para https://www.viewgrip.net/.

* **ejemplo_posicion.py** Ejemplo de un scpript que te preporciona por la pantalla las coordenadas dónde has realizado click. 

* **ejemplo_lectura_teclado_a_fichero.py** Ejemplo de bot para la lectura del teclado y almacenar en un fichero.

* **bot_viewgrip_imagenes_ejecucion.py** Ejemplo de bot para lanzar automáticamente el cliente de viewgrip. 

### Prerequisites

```
pynput
#importante tenerle actualizado.
#python -m pip install --upgrade pip 
scikit-build
opencv-python
numpy
python3_xlib
pyautogui
mss
pytesseract
screen_search
# para python3.7 en ubuntu necesairo es necesario. 
#sudo apt-get install python3.7-tk
```

### Installing
Para ejecutar este proyecto es necesario ejecutar el siguiente comando y añadir las credenciales de acceso a la api de twitter. 

```
python get-pip.py install -r requirements.txt
git clone --depth=1 https://github.com/twintproject/twint.git
cd twint
python get-pip.py  install . -r requirements.txt
```
o en el caso de linux

```
pip install -r requirements.txt
git clone --depth=1 https://github.com/twintproject/twint.git
cd twint
pip3 install . -r requirements.txt
```

## Authors
* Rubén Pérez Ibáñez

## License
Released Under CC BY-SA 4.0 License
