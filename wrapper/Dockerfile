# Verwenden Sie ein offizielles Python-Image als Basis
FROM python:3.8

# Setzen Sie das Arbeitsverzeichnis im Container
WORKDIR /app

# Installieren Sie Piper TTS und Abhängigkeiten
RUN pip install piper-tts piper-phonemize==1.1.0

# Kopieren Sie Ihr Python-Skript in das Container-Image
COPY run.py ./

# Führen Sie das Skript beim Start des Containers aus
CMD ["python", "./run.py"]
