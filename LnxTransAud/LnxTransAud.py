import os
import json
import pyaudio
import sys
from vosk import Model, KaldiRecognizer, SetLogLevel
from deep_translator import GoogleTranslator

# Silencia logs internos do Vosk
SetLogLevel(-1)

MODEL_PATH = "model"
if not os.path.exists(MODEL_PATH):
    print(f"Erro: Pasta '{MODEL_PATH}' não encontrada.")
    sys.exit(1)

# Inicialização silenciosa
model = Model(MODEL_PATH)
rec = KaldiRecognizer(model, 16000)
translator = GoogleTranslator(source='en', target='pt')

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, 
                input=True, frames_per_buffer=8000)
stream.start_stream()

# Loop principal
while True:
    data = stream.read(4000, exception_on_overflow=False)
    if len(data) == 0:
        break
    
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        text = result.get("text", "")
        
        if text:
            try:
                # Traduz e exibe apenas o Português
                translated = translator.translate(text)
                print(translated)
            except:
                pass # Ignora erros de conexão na tradução
