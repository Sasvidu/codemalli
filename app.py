import gradio as gr
from faster_whisper import WhisperModel
from gtts import gTTS
# from langdetect import detect
import os
import uuid
import os
from detect import detect_si_en
from generate_explanation import generate_explanation

# Create audio directory if it doesn't exist
os.makedirs("audio", exist_ok=True)

# Load model
model = WhisperModel("small", compute_type="int8")

def transcribe_and_teach(audio):
    print("[INFO] Starting transcription...")
    segments, _ = model.transcribe(audio)
    transcription = " ".join([seg.text for seg in segments])
    print(f"[INFO] Transcription: {transcription}")

    # Detect language
    try:
        lang = detect_si_en(transcription)
        print(f"[INFO] Detected language: {lang}")
    except Exception as e:
        print(f"[ERROR] Language detection failed: {e}")
        lang = "unknown"
    
    # Generate explanation
    try:
        print("[INFO] Generating explanation...")
        ai_explanation = generate_explanation(transcription)
        # ai_explanation = "Hello!"
        print(f"[INFO] Explanation generated: {ai_explanation}")
    except Exception as e:
        print(f"[ERROR] Explanation generation failed: {e}")
        ai_explanation = "Oops! Couldn't generate explanation."

# Translate if Sinhala detected (placeholder)
    if lang == "si":
        try:
            print("[INFO] Translating explanation to Sinhala (placeholder)...")
            translated_text, tts_lang = translate_en_to_si(ai_explanation_en)
            print(f"[INFO] Placeholder translation output: {translated_text}, lang: {tts_lang}")
            final_explanation = translated_text
        except Exception as e:
            print(f"[ERROR] Translation failed: {e}")
            final_explanation = ai_explanation_en
            tts_lang = "en"
    else:
        final_explanation = ai_explanation_en
        tts_lang = "en"

    # Generate audio response
    try:
        print("[INFO] Converting to speech...")
        tts = gTTS(text=final_explanation, lang=tts_lang)
        filename = f"audio/{uuid.uuid4()}.mp3"
        tts.save(filename)
        print(f"[INFO] Audio saved as: {filename}")
    except Exception as e:
        print(f"[ERROR] TTS failed: {e}")
        filename = None
    
    return transcription, lang, ai_explanation, filename


iface = gr.Interface(
    fn=transcribe_and_teach,
    inputs=gr.Audio(type="filepath"),
    outputs=[
        gr.Textbox(label="Transcription"),
        gr.Textbox(label="Detected Language (ISO code)"),
        gr.Textbox(label="Explanation"),
        gr.Audio(label="Audio Response")
    ],
    title="සිංහල AI Tech Tutor"
)

iface.launch()
