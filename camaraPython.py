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

#cerramos la cámara
camera.release()
cv2.destroyAllWindows()
print("video detenido")