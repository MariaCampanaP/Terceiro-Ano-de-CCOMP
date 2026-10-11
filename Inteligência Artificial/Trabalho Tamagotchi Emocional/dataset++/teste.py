import numpy as np
import cv2
import pandas as pd
from tensorflow.keras.models import load_model
import serial
import time
from pathlib import Path

arduino = serial.Serial('COM13', 9600, timeout=1)
time.sleep(2) # Aguarda a conexão estabilizar


IMG_SIZE = 48

MODEL_PATH = Path(__file__).with_name('modelo.keras')
modelo = load_model(str(MODEL_PATH)) #importa o modelo treinado

# abre webcam
camera = cv2.VideoCapture(0)

contador = 0

while True:
    

    ret, frame = camera.read()

    contador += 1

    if contador % 10 == 0:

        img = cv2.resize(
            frame,
            (IMG_SIZE, IMG_SIZE)
        )
        
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converte para escala de cinza

        img = img.astype(
            "float32"
        ) / 255.0

        img = np.expand_dims(
            img,
            axis=0
        )
        
        img = np.expand_dims(
            img,
            axis=-1
        )

        pred = modelo.predict(
            img,
            verbose=0
        )[0]

        classe = np.argmax(pred)
        print("\nProbabilidades:")
        print("Happy:", pred[0])
        print("Angry:", pred[1])
        print("Sad:", pred[2])

        pred = np.max(pred)

        if classe == 0:
            texto = f"HAPPY ({pred:.2f})"
            arduino.write(b'1')
        elif classe == 1:
            texto = f"ANGRY ({pred:.2f})"
            arduino.write(b'2')
        else:
            texto = f"SAD ({pred:.2f})"
            arduino.write(b'3')
        cv2.putText(
            frame,
            texto,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow(
            "Classificador de Expressões",
            frame
        )

        # ESC para sair
        if cv2.waitKey(1) & 0xFF == 27:
            break

camera.release()
#arduino.close()
cv2.destroyAllWindows()