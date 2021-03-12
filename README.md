<h1 align="center">
    Abrir camara web con Python y OpenCV
</h1>
<p>
    En este tutorial vamos a ver como adquirir y mostrar imágenes de una     cámara usando OpenCV y python. OpenCV ofrece varias alternativas         para conectarse a una cámara a traves de la función cv2.VideoCapture().
</p>

```python
import cv2

camera = cv2.VideoCapture()

""" 
camera.open(0) -> el nuero de cámaras que se tiene conectado
camera.open(1) -> el nuero de cámaras que se tiene conectado
.
.
.
camera.open(n) -> el nuero de cámara que se tiene conectado
"""
camera.open(1)
ret, frame = camera.read()
# se muestra la imagen 
cv2.imshow('frame', frame)
# presionar la tecla Q para cerrar la ventana
cv2.waitKey(0)
# cerrar la cámara
camera.release()
cv2.destroyAllWindows()
print("video detenido")
```
<h2>
    Capturar Video de la cámara
</h2>

```python
import cv2

camera = cv2.VideoCapture()
camera.open(1)

while True:
    # capturar frame a frame
    ret, frame = camera.read()
    # si el frame se captura correctamente ret es True
    if not ret:
        print("no se pudo capurar la imagen")
        break
    # se muestra el frame
    cv2.imshow('frame', frame)
    #presionamos la tecla Q para cerrar la ventana
    if cv2.waitKey(1) == ord('q'):
        break
# cerrar la cámara
camera.release()
cv2.destroyAllWindows()
print("video detenido")
```