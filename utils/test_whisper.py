import whisper

# Cargar el modelo base (puedes cambiar a "tiny" si quieres que sea más rápido)
model = whisper.load_model("base")

# Ruta al archivo de audio que ya grabaste
audio_path = "user_voice.wav"  # asegúrate de que esté en la raíz del proyecto o cambia la ruta

print("🔍 Transcribiendo...")
result = model.transcribe(audio_path)

print("📝 Transcripción:")
print(result["text"])
