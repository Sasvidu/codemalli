import gradio as gr
from faster_whisper import WhisperModel
from gtts import gTTS
from langdetect import detect
import os
import uuid
import os

# Create audio directory if it doesn't exist
os.makedirs("audio", exist_ok=True)

# Load model
model = WhisperModel("small", compute_type="int8")

def transcribe_and_teach(audio):
    segments, _ = model.transcribe(audio)
    transcription = " ".join([seg.text for seg in segments])

    # Detect language (default to 'unknown' if detection fails)
    try:
        lang = detect(transcription)
    except:
        lang = "unknown"
    
    # Dummy Sinhala answer for now
    sinhala_response = "ඔබගේ ප්‍රශ්නය වටහාගත්තා. මෙන්න උත්තරය..."

    # Text to speech
    tts = gTTS(text=sinhala_response, lang="si")
    filename = f"audio/{uuid.uuid4()}.mp3"
    tts.save(filename)
    
    return transcription, lang, sinhala_response, filename

iface = gr.Interface(
    fn=transcribe_and_teach,
    inputs=gr.Audio(type="filepath"),
    outputs=[
        gr.Textbox(label="Transcription"),
        gr.Textbox(label="Detected Language (ISO code)"),
        gr.Textbox(label="Sinhala Answer"),
        gr.Audio(label="Audio Response")
    ],
    title="සිංහල AI Tech Tutor"
)

iface.launch()
