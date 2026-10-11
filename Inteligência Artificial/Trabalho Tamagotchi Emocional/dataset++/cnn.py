import numpy as np
import cv2
from tensorflow.keras.models import load_model

IMG_SIZE = 48

modelo = load_model('modelo.keras') #importa o modelo treinado

# detector de rosto (Haar Cascade)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# abre webcam
camera = cv2.VideoCapture(0)

contador = 0
texto = ""

while True:

    ret, frame = camera.read()
    if not ret:
        break

    gray_full = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_full, scaleFactor=1.1, minNeighbors=5)

    contador += 1

    for (x, y, w, h) in faces:
        # desenha o retângulo do rosto detectado
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) # desenha um retângulo azul, só visual, para confirmar se a detecção está funcionando

        if contador % 10 == 0:
            rosto = gray_full[y:y+h, x:x+w]  # recorta apenas a região do rosto da imagem já em cinza
            rosto = cv2.resize(rosto, (IMG_SIZE, IMG_SIZE))
            rosto = rosto.astype("float32") / 255.0
            rosto = np.expand_dims(rosto, axis=0)
            rosto = np.expand_dims(rosto, axis=-1)

            pred = modelo.predict(rosto, verbose=0)[0]
            classe = np.argmax(pred)
            confianca = np.max(pred)

            print("\nProbabilidades:")
            print("Happy:", pred[0])
            print("Angry:", pred[1])
            print("Sad:", pred[2])

            rotulos = ["HAPPY", "ANGRY", "SAD"]
            texto = f"{rotulos[classe]} ({confianca:.2f})"

        if texto:
            cv2.putText(frame, texto, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Classificador de Expressoes", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()