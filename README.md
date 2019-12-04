# Proyecto Traductor de Lengua de Signos

_El objetivo del proyecto es desarrollar una aplicación para niños (o cualquier persona) que necesiten (o quieran) aprender desde cero la lengua de signos. Con una cámara se detecta el signo que la persona hace con su mano y el programa debe ser capaz de identificarlo, en tiempo real. En un inicio sería algo sencillo, como por ejemplo detectar letras y números._

## Comenzando 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

El archivo para detectar letras es **segment_vgg19_dia22_miguel.py** y el que detecta números es **segment_modelmiguelnumber.py**.


### Pre-requisitos 📋

_¿Qué necesitas para poder correr los códigos?_

Necesitas instalar Anaconda y Spyder. Quizás también instalar algunos paquetes de python. Y luego en la consola de comandos simplemente llamar a las funciones.

Para las letras:
```
python segment_vgg19_dia22_miguel.py
```

Para los números:
```
python segment_modelmiguelnumber.py
```

### Datos 🖼
El datset utlizado para entrenar el modelo de reconocimiento de letras está compuesto por tres datasets distintos representando cada una de las letras de la lengua de signos americana:
* "ASL Alphabet" colgado por Akash en Kaggle (https://www.kaggle.com/grassknoted/asl-alphabet)
* "ASL Alphabet Test" colgado por Dan Rasband también en Kaggle (https://www.kaggle.com/danrasband/asl-alphabet-test)
* Dataset creado específicamente para este proyecto 
<p float="left">
  <img src="https://github.com/ecabestadistica/sign-language-translator-python-opencv/blob/master/IMG_0020.JPG" width="250" />
  <img src="https://github.com/ecabestadistica/sign-language-translator-python-opencv/blob/master/IMG_0640.JPG" width="250" /> 
  <img src="https://github.com/ecabestadistica/sign-language-translator-python-opencv/blob/master/IMG_1482.JPG" width="250" />
</p>

Para entrenar el modelo de reconocimiento de números se utilzó:
* "Sign Language Digits Dataset" colgado por Arda Mavi en Kaggle (https://www.kaggle.com/ardamavi/sign-language-digits-dataset)

En ambos casos se efectuó una aumentación de datos que incluía:
* Normalización de los datos
* Transvecciones
* Ampliaciones
* Desplazamientos laterales y verticales
* Modificación de brillo

Finalmente, el dataset fue segemtando en dos partes (80/20), una de entrenamiento y otra de validación para poder detectar si el modelo se sobreajuista a los datos. 


### Modelo

### Aplicación 🤓

_¿En qué consiste la aplicación?_

<p align="center">
    <img src="elinumeros.gif", width="450">
</p>

Se abrirá una ventana donde se puede ver en tiempo real las imágenes captadas por la webcam. En un recuadro verde que aparece, el usuario deberá representar el signo (letra o número según el programa) y en tiempo real obtendrá la clasificación. La imagen recortada que está dentro de los límites del recuadro verde será el input del modelo. Y el output será a qué signo corresponde.

Para ayudar a los nuevos usuarios (no olvidemos que el objetivo es aprender lengua de signos), aparecerá una ventana pequeña con sugerencias de signos reales y a qué letra o número corresponde. Esta funcionalidad aparece al tocar la tecla "Espacio". Para cambiar de signo, volver a tocar "Espacio".
El cambio lo hará de manera aleatoria. 

Aparecerán debajo del recuadro verde también las clasificaciones por el modelo que queden en 2do o 3er lugar, porque por ejemplo hay letras que se parecen mucho: A, E y S o K y V. Con lo cual si no queda en 1ra posición, se puede observar si por lo menos queda en 2da o 3ra posición.

