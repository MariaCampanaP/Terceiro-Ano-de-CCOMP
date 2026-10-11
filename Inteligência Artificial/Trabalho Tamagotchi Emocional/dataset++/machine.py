import os
import zipfile
import numpy as np
import gdown
import cv2

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.utils.class_weight import compute_class_weight

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

IMG_SIZE = 48
CHANNELS = 1
NUM_CLASSES = 4


def download_dataset(url, arquivo_zip="emotions1.zip", pasta_destino="emotions"):
    classes_esperadas = ("neutral", "happy", "angry", "sad")

    if all(os.path.isdir(os.path.join(pasta_destino, classe)) for classe in classes_esperadas):
        return pasta_destino

    gdown.download(url, arquivo_zip, quiet=False)

    if not os.path.exists(arquivo_zip):
        raise RuntimeError("Não foi possível baixar o dataset.")

    with zipfile.ZipFile(arquivo_zip, 'r') as zip_ref:
        zip_ref.extractall(".")

    return pasta_destino


def extrair_atributos(caminho_imagem):
    img = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)

    if img is None:
        return None

    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img.astype("float32") / 255.0

    return img


def carregar_imagens_de_pasta(caminho_base, mapa_classes):
    X = []
    y = []

    for nome_pasta, label in mapa_classes.items():
        pasta = os.path.join(caminho_base, nome_pasta)

        if not os.path.isdir(pasta):
            continue

        for arquivo in os.listdir(pasta):
            if arquivo.lower().endswith((".jpg", ".jpeg", ".png")):
                caminho_img = os.path.join(pasta, arquivo)
                imagem = extrair_atributos(caminho_img)

                if imagem is not None:
                    X.append(imagem)
                    y.append(label)

    return X, y


def carregar_dataset_principal(caminho_base):
    # Dataset emotions:
    # neutral = 0
    # happy = 1
    # angry = 2
    # sad = 3

    mapa_emotions = {
        "happy": 0,
        "angry": 1,
        "sad": 2
    }

    return carregar_imagens_de_pasta(caminho_base, mapa_emotions)


def carregar_ck_secundario(caminho_ck):
    # CK+:
    # happy 1
    # anger 2
    # sadness 3
    
    mapa_ck = {
        "happy": 0,
        "anger": 1,
        "sadness": 2
    }

    return carregar_imagens_de_pasta(caminho_ck, mapa_ck)


def juntar_datasets(caminho_emotions, caminho_ck=None):
    X1, y1 = carregar_dataset_principal(caminho_emotions)

    X_total = X1
    y_total = y1

    if caminho_ck is not None and os.path.isdir(caminho_ck):
        X2, y2 = carregar_ck_secundario(caminho_ck)
        X_total += X2
        y_total += y2

        print("CK+ adicionado como secundário.")
        print("Imagens adicionadas do CK+:", len(X2))
    else:
        print("CK+ não encontrado. Usando apenas o dataset principal.")

    X_total = np.array(X_total)
    y_total = np.array(y_total)

    X_total = X_total.reshape(-1, IMG_SIZE, IMG_SIZE, CHANNELS)

    return X_total, y_total


def dividir_dados(X, y, porcentagem_teste, random_state):
    return train_test_split(
        X,
        y,
        test_size=porcentagem_teste,
        stratify=y,
        random_state=random_state
    )


def gerar_modelo():
    modelo = Sequential()

    modelo.add(Conv2D(32, (3, 3), activation="relu", padding="same",
                      input_shape=(IMG_SIZE, IMG_SIZE, CHANNELS)))
    modelo.add(BatchNormalization())
    modelo.add(MaxPooling2D((2, 2)))
    modelo.add(Dropout(0.25))

    modelo.add(Conv2D(64, (3, 3), activation="relu", padding="same"))
    modelo.add(BatchNormalization())
    modelo.add(MaxPooling2D((2, 2)))
    modelo.add(Dropout(0.25))

    modelo.add(Conv2D(128, (3, 3), activation="relu", padding="same"))
    modelo.add(BatchNormalization())
    modelo.add(MaxPooling2D((2, 2)))
    modelo.add(Dropout(0.35))

    modelo.add(Flatten())

    modelo.add(Dense(128, activation="relu"))
    modelo.add(Dropout(0.5))

    modelo.add(Dense(NUM_CLASSES, activation="softmax"))

    return modelo


def avaliacao(modelo, X_teste, y_teste):
    y_prob = modelo.predict(X_teste)
    y_pred = np.argmax(y_prob, axis=1)

    acc = accuracy_score(y_teste, y_pred)
    nomes_classes = ["happy", "angry", "sad"]

    print(f"\nAcurácia geral: {acc:.2%}\n")

    # Relatório em formato de tabela mais legível
    relatorio = classification_report(
        y_teste,
        y_pred,
        target_names=nomes_classes,
        output_dict=True
    )

    print(f"{'Classe':<12}{'Precisão':>10}{'Recall':>10}{'F1-score':>10}{'Suporte':>10}")
    print("-" * 52)
    for classe in nomes_classes:
        m = relatorio[classe]
        print(f"{classe:<12}{m['precision']:>10.2%}{m['recall']:>10.2%}{m['f1-score']:>10.2%}{int(m['support']):>10}")
    print("-" * 52)
    print(f"{'Acurácia':<12}{'':>10}{'':>10}{acc:>10.2%}{int(relatorio['macro avg']['support']):>10}")

    # Matriz de confusão como heatmap
    matriz = confusion_matrix(y_teste, y_pred)

    plt.figure(figsize=(6, 5))
    sns.heatmap(
        matriz,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=nomes_classes,
        yticklabels=nomes_classes,
        cbar=True
    )
    plt.xlabel("Previsto")
    plt.ylabel("Real")
    plt.title(f"Matriz de Confusão (Acurácia: {acc:.1%})")
    plt.tight_layout()
    plt.savefig("matriz_confusao.png", dpi=150)
    plt.show()

def plotar_historico(historico):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 5))
    
    ax1.plot(historico.history['accuracy'], label = 'Treino')
    ax1.plot(historico.history['val_accuracy'], label = 'Validação')
    ax1.set_title('Acurácia por época')
    ax1.set_xlabel('Época')
    ax1.set_ylabel('Acurácia')
    ax1.legend()
    ax1.grid(alpha = 0.3)
    
    ax2.plot(historico.history['loss'], label = 'Treino')
    ax2.plot(historico.history['val_loss'], label = 'Validação')
    ax2.set_title('Loss por época')
    ax2.set_xlabel('Época')
    ax2.set_ylabel('Loss')
    ax2.legend()
    ax2.grid(alpha = 0.3)
    
    plt.tight_layout()
    plt.savefig("historico_treinamento.png", dpi = 150)
    plt.show()
    
# Dataset principal
dataset_url = "https://drive.google.com/file/d/1i--URvAJ4MbRysQ7E0oLFhmhuG9ZjGVd/view?usp=sharing"
base_dataset_path = download_dataset(dataset_url)

# Pasta do CK+ secundário
# Ajuste esse caminho se a sua pasta tiver outro nome.
caminho_ck = "ckextended"

X, y = juntar_datasets(base_dataset_path, caminho_ck)

print("Formato X:", X.shape)
print("Formato y:", y.shape)
print("Classes:", np.unique(y))
print("Quantidade por classe:", np.bincount(y))

X_treino, X_teste, y_treino, y_teste = dividir_dados(X, y, 0.2, 25)

classes = np.unique(y_treino)

pesos = compute_class_weight(
    class_weight="balanced",
    classes=classes,
    y=y_treino
)

class_weights = dict(zip(classes, pesos))

modelo = gerar_modelo()

opt_adam = Adam(learning_rate=0.0005)

modelo.compile(optimizer=opt_adam, loss="sparse_categorical_crossentropy", metrics=["accuracy"])

early_stop = EarlyStopping(monitor="val_loss",patience=6,restore_best_weights=True)

historico = modelo.fit(X_treino,y_treino,epochs=40,batch_size=64, validation_split=0.1, class_weight=class_weights,callbacks=[early_stop])

modelo.save("modelo.keras")

plotar_historico(historico)

avaliacao(modelo, X_teste, y_teste)