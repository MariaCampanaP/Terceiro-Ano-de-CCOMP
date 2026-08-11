import numpy as np
import souddevice as sd
import librosa
import joblib
import noisereduce as nr

from tensorflow.keras.models import load_model

SAMPLE_RATE = 22050

DURATION = 3 #Segundos

def extrair_atributos(audio):
  mfcc = librosa.feature.mfcc(
      y = audio,
      sr = SAMPLE_RATE,
      n_mfcc = 40
  )
  mfcc_mean = np.mean(
      mfcc.T,
      axis = 0
  )

  return mfcc_mean

def melhora_audio(audio):
  audio, _ = librosa.effects.trim(
        audio,
        top_db=20
  )
  audio = nr.reduce_noise(
      y = audio,
      sr = SAMPLE_RATE
  )

  return audio

modelo = load_model(
    "teste/modelo_emocoes.h5"
)

while True:
  input(
      "\nPressione ENTER para gravar áudio..."
  )
  print("GRAVANDO ÁUDIO...")

  #Grava áudio
  audio = sd.red(
      int(DURATION * SAMPLE_RATE),
      samplerate = SAMPLE_RATE,
      channels = 1,
      dtype = "float32"
  )

  sd.wait()

  print("\nGravação finalizada!")

  audio = audio.flatten()

  audio = audio / np.max(
      np.abs(audio)
  )

  audio = melhora_audio(audio)
  atributos = extrair_atributos(audio)

  #predicao
  #resultado