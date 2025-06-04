# CodeMalli — Bilingual AI Tech Tutor for Sri Lankan Students]

---

## 📖 Overview

**CodeMalli** is a lightweight, Python-based AI-powered voice assistant web app designed to act as a bilingual (Sinhala & English) tech tutor for students in Sri Lanka. It helps beginners understand fundamental programming and technology concepts using voice or text input, providing simple, clear explanations and Sinhala voice responses.

---

## 🎯 Phase 1 (MVP) Features

- 🎤 Voice Input via microphone (and audio file fallback)  
- ✍️ Text Input fallback option  
- 🧠 AI-based beginner-friendly explanations on tech concepts such as:  
  - Variables, APIs, Cloud Computing, DevOps, Intel Thread Director, etc.  
- 🌐 Automatic language detection (Sinhala or English) on user input  
- 🌍 Sinhala language response output:  
  - Text displayed on UI  
  - Spoken response using Sinhala Text-to-Speech (gTTS)  
- 💻 Runs locally on macOS (Apple Silicon M1/M2), designed for CPU-only usage  
- 🧰 Built with Python 3, Gradio UI, Faster Whisper for speech recognition, and transformer-based or OpenAI models for explanation generation  
- 🧩 Modular code structure ready for future upgrades

---

## ⚙️ Technologies Used

- Python 3.11+  
- [Gradio](https://gradio.app/) — User interface with mic and text input  
- [faster-whisper](https://github.com/guillaumekln/faster-whisper) — Offline speech-to-text engine  
- [gTTS](https://pypi.org/project/gTTS/) — Sinhala text-to-speech synthesis  
- [transformers](https://huggingface.co/docs/transformers/index) — AI models for explanation generation (optional OpenAI API integration)  
- [langdetect](https://pypi.org/project/langdetect/) — Language detection  
- FFmpeg (installed via Homebrew) for audio processing support  

---

## 🗂 Project Structure

├── app.py # Main application code
├── audio/ # Folder to store generated TTS audio files
├── requirements.txt # Python dependencies
└── README.md # This file


---

## 🚀 Getting Started (Phase 1)

1. Clone the repo  
2. Create and activate a Python virtual environment  
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   brew install ffmpeg        # macOS only, if not already installed
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open http://127.0.0.1:7860 in your browser
6. Use the microphone or text input to ask tech questions in Sinhala or English
7. Receive simple Sinhala explanations via text and audio

