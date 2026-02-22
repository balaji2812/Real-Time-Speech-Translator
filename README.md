# 🎙️ Real-Time Speech Translator

## 📌 Overview

This project implements a real-time Tamil to English speech-to-speech translation system using speech recognition and generative AI.

The application captures Tamil speech input through a microphone, converts it into text using speech recognition, translates the text into English using Google's Gemini AI model, and outputs the translated result as spoken English using text-to-speech synthesis.

This project demonstrates integration of AI APIs, real-time audio processing, and secure API handling.

---

## 🚀 Features

- 🎤 Real-time Tamil speech recognition  
- 🌍 AI-powered translation using Gemini API  
- 🔊 English speech output (Text-to-Speech)  
- 🔐 Secure API key handling using environment variables  
- ⚡ Low-latency voice processing  

---

## 🛠️ Tech Stack

- Python  
- SpeechRecognition  
- Google Generative AI (Gemini)  
- pyttsx3  
- PyAudio  

---

## 📂 Project Structure

```text
Tamil-English-Voice-Translator/
│
├── ts.py
├── requirements.txt
├── README.md
└── .gitignore

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Tamil-English-Voice-Translator.git
cd Tamil-English-Voice-Translator
```

---

### 2️⃣ Create Virtual Environment (Recommended)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Setup

This project uses Google's Gemini API.

You must set your API key as an environment variable.

### Windows (PowerShell):

```bash
$env:API_KEY="your_api_key_here"
```

### Mac/Linux:

```bash
export API_KEY="your_api_key_here"
```

⚠️ Do NOT hardcode your API key inside the source code.

---

## ▶️ How to Run the Application

```bash
python ts.py
```

When prompted:
- Enter `1` to start speaking
- Enter `0` to exit

Speak in Tamil when asked.

The system will:
1. Convert your speech to Tamil text  
2. Translate it into English  
3. Speak the translated English output  

---

## 🧠 How It Works

1. SpeechRecognition captures microphone audio.
2. Google Speech Recognition converts speech to Tamil text.
3. The Tamil text is sent to Gemini AI model.
4. The AI model translates Tamil to English.
5. pyttsx3 converts translated English text into speech.

---

## 📸 Example Output

```
Speak in Tamil now...
[Source Tamil Text]: நான் பள்ளிக்குச் செல்கிறேன்
Translating...
[Translated English Text]:
I am going to school.
Speaking translation...
```

---

## 📈 Future Improvements

- Multi-language support
- Web-based interface using Flask
- Reduce latency
- Add GUI
- Deploy as web application

---

## 👨‍💻 Author

Balaji B P  
B.Tech CSE (IoT & Automation)  
AI/ML & IoT Enthusiast  
