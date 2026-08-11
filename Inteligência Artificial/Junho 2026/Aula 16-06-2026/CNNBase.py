import os
import zipfile
import numpy as np
import gdown
import cv2

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.optimizers import Adam

IMG_SIZE = 64
CHANNELS = 3 # RGB images


def download_dataset(url, arquivo_zip="dogs_cats.zip"):
    gdown.download(
        url,
        arquivo_zip,
        fuzzy=True,
        quiet=False
    )
    zip_referencia = zipfile.ZipFile(arquivo_zip,'r')
    zip_referencia.extractall(".")
    zip_referencia.close()
    return os.path.join(".", "dogs_cats")

def extrair_atributos(caminho_imagem):
    img = cv2.imread(caminho_imagem)
    if img is None:
      return None
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img.astype('float32') / 255.0 # Normaliza os pixel para valores entre [0, 1]
    return img

def carregar_dados(caminho_base):
    X = []
    y = []

    # dogs = 0
    pasta_dogs = os.path.join(caminho_base, "dogs")
    for arquivo in os.listdir(pasta_dogs):
        if arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            caminho_completo = os.path.join(pasta_dogs, arquivo)
            atributos = extrair_atributos(caminho_completo)
            if atributos is not None:
                X.append(atributos)
                y.append(0)

    # cats = 1
    pasta_cats = os.path.join(caminho_base, "cats")
    for arquivo in os.listdir(pasta_cats):
        if arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            caminho_completo = os.path.join(pasta_cats, arquivo)
            atributos = extrair_atributos(caminho_completo)
            if atributos is not None:
                X.append(atributos)
                y.append(1)

    X = np.array(X)
    y = np.array(y)
    return X, y

def dividir_dados(X, y, porcentagem_teste, random_state):
  X_treino, X_teste, y_treino, y_teste = train_test_split(
      X,
      y,
      test_size=porcentagem_teste,
      stratify = y, #ponto importante
      random_state=random_state)
  return X_treino, X_teste, y_treino, y_teste


def gerar_modelo():
  modelo = Sequential()
  modelo.add(Conv2D(32, (5, 5), activation = 'relu', padding = 'same', input_shape = (IMG_SIZE, IMG_SIZE, CHANNELS)))
  modelo.add(MaxPooling2D((2, 2)))

  modelo.add(Conv2D(34, (5, 5), activation = 'relu'))
  modelo.add(MaxPooling2D((2, 2)))

  modelo.add(Flatten())
  modelo.add(Dense(120, activation = 'relu'))
  modelo.add(Dense(84, activation = 'relu'))
  modelo.add(Dense(2, activation = 'softmax'))
  modelo.add(Dropout(0.2))

  return modelo

def avaliacao(modelo, X_teste, y_teste):
    y_prob = modelo.predict(X_teste)
    y_pred = np.argmax(y_prob, axis=1) # Get the class with the highest probability
    acc = accuracy_score(y_teste, y_pred)
    print("Acurácia:", acc)


dataset_url = "https://drive.google.com/file/d/1c2K2n8VH69RY1KOXDViJ4lsqpYeCPd4Z/view?usp=sharing"
#dataset_url = "https://drive.google.com/file/d/1AcVLQAdIC0r79BBPcKnT6NQmYyr3o2w0/view?usp=sharing"
base_dataset_path = download_dataset(dataset_url)
X, y = carregar_dados(base_dataset_path)
X_treino, X_teste, y_treino, y_teste = dividir_dados(X, y, 0.2, 25)
modelo = gerar_modelo()

opt_adam = Adam(learning_rate=0.001)

modelo.compile(optimizer = opt_adam, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
modelo.fit(X_treino, y_treino, epochs=20, batch_size=32, validation_split=0.1)
modelo.save('gatos_e_cachorros.h5')
avaliacao(modelo, X_teste, y_teste)