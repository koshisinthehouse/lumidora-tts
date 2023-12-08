from pydub import AudioSegment
import os
# Erstelle den Ordner, falls er nicht existiert
# Pfad zum Ordner, in dem sich die WAV-Dateien befinden
wav_folder_path = "wav"  # Ersetze dies mit dem tatsächlichen Pfad
if not os.path.exists(wav_folder_path):
    os.makedirs(wav_folder_path)
    print("Verzeichnis 'wav' wurde erstellt.")
else:
    print("Verzeichnis 'wav' existiert bereits.")

import json
from urllib import request, parse

def send_sentence(sentence, url="http://localhost:7862/api/tts"):
    data = json.dumps({
        "text": sentence,
        "voice": "domoskanonos.onnx"
    }).encode()

    req = request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    with request.urlopen(req) as response:
        if response.status == 200:
            return response.read()
        else:
            raise Exception(f"Anfrage fehlgeschlagen mit Statuscode: {response.status}")

    
def save_audio_from_response(audio_content, filename):
    with open(filename, 'wb') as file:
        file.write(audio_content)

def split_text_into_sentences(text):
    sentences = text.split(".")
    return [s.strip() + "." for s in sentences if s.strip()]

# Lade den Text aus einer Datei
with open("./story.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Splitte den Text in Sätze
sentences = split_text_into_sentences(text)

# Sende jeden Satz und speichere die Antwort als Audiofile
for i, sentence in enumerate(sentences):
    try:
        audio_content = send_sentence(sentence)
        filename = f"wav/sentence_{i+1}.wav"
        save_audio_from_response(audio_content, filename)
        print(f"Audio für Satz {i+1} gespeichert als {filename}")
    except Exception as e:
        print(f"Fehler beim Senden von Satz {i+1}: {e}")


import os
from pydub import AudioSegment

def combine_wav_files(file_list, output_filename):
    combined = AudioSegment.empty()
    for file in file_list:
        audio = AudioSegment.from_wav(file)
        combined += audio
    combined.export(output_filename, format="wav")


# Funktion zum Löschen aller Dateien in einem Verzeichnis, außer einer spezifizierten Datei
def delete_files_except(wav_folder_path, except_file):
    for f in os.listdir(wav_folder_path):
        file_path = os.path.join(wav_folder_path, f)
        if os.path.isfile(file_path) and f != except_file:
            os.remove(file_path)
            print(f"Datei {f} gelöscht.")


# Liste alle WAV-Dateien im Ordner auf
wav_files = [os.path.join(wav_folder_path, f) for f in os.listdir(wav_folder_path) if f.endswith('.wav')]

# Dateien zusammenfügen
combine_wav_files(wav_files, "combined_output.wav")

# Rückmeldung, dass der Vorgang abgeschlossen ist
print("Alle WAV-Dateien wurden zu 'combined_output.wav' zusammengefügt.")

# Lösche alle Dateien im wav-Ordner, außer 'combined_output.wav'
delete_files_except(wav_folder_path, "combined_output.wav")

# Lade die WAV-Datei
wav_audio = AudioSegment.from_file("./combined_output.wav", format="wav")

# Konvertiere in MP3
wav_audio.export("./output.mp3", format="mp3")