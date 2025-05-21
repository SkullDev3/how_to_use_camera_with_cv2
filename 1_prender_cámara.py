import cv2  # exportamos la libreria que nos permita usar la cámara

# buscamos la cámara disponible, puede ser de 0,1,2,3,4,5...
# si quisiera poner ip cambio en lugar de 0 por https//
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # audio, video=leer información de la cámara
    cv2.imshow("Video", frame)  # mostrar video

    k = cv2.waitKey(1)  # esperar 1 segundo al pulsar la tecla

    if k == ord('h'):
        break

cap.release()

cv2.destroyAllWindows()
