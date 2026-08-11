import os
import zipfile
import numpy as np
import librosa
import gdown
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


def download_dataset(url, arquivo_zip="ravdess.zip"):
    gdown.download(
        url,
        arquivo_zip,
        fuzzy=True,
        quiet=False
    )
    zip_referencia = zipfile.ZipFile(arquivo_zip,'r')
    zip_referencia.extractall(".")
    zip_referencia.close()
    return os.path.join(".", "ravdess_filtrado")


def extrair_atributos(caminho_audio):
    audio, sr = librosa.load(
        caminho_audio,
        sr=22050
    )
    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=40
    )
    return np.mean(mfcc.T, axis=0)

def carregar_dados(caminho_base):
    X = []
    y = []

    # SAD = 0
    pasta_sad = os.path.join(caminho_base, "sad")
    for arquivo in os.listdir(pasta_sad):
        if arquivo.endswith(".wav"):
            caminho = os.path.join(pasta_sad, arquivo)
            atributos = extrair_atributos(caminho)
            X.append(atributos)
            y.append(0)

    # HAPPY = 1
    pasta_happy = os.path.join(caminho_base, "happy")
    for arquivo in os.listdir(pasta_happy):
        if arquivo.endswith(".wav"):
            caminho = os.path.join(pasta_happy, arquivo)
            atributos = extrair_atributos(caminho)
            X.append(atributos)
            y.append(1)
    X = np.array(X)
    y = np.array(y)
    return X, y

def dividir_dados(X, y, porcentagem_teste, random_state):
  X_treino, X_teste, y_treino, y_teste =  train_test_split(X, y, test_size = porcentagem_teste, random_state = random_state)
  return X_treino, X_teste, y_treino, y_teste

def gerar_modelo():
  modelo = Sequential()
  modelo.add(Dense(128, activation = 'relu', input_shape = (40, )))
  modelo.add(Dense(64, activation = 'relu'))
  modelo.add(Dense(1, activation = 'relu'))

  return modelo

def avaliacao(modelo, X_teste, y_teste):
    y_prob = modelo.predict(X_teste)
    y_pred = (y_prob > 0.5).astype(int)
    acc = accuracy_score(y_teste, y_pred)
    print("Acurácia:", acc)


dataset_url = "https://drive.google.com/file/d/1cfLOTCwoB7tBprcWPP0Zf7Sq7z2Ae9sO/view?usp=sharing"
base_dataset_path = download_dataset(dataset_url)
X, y = carregar_dados(base_dataset_path)
X_treino, X_teste, y_treino, y_teste = dividir_dados(X, y, 0.2, 25)
dividir_dados(X, y, 0.2, 25)
modelo = gerar_modelo()
modelo.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
modelo.fit(X_treino, y_treino, epochs = 30)
modelo.save('emocoes.keras')
avaliacao(modelo, X_teste, y_teste)