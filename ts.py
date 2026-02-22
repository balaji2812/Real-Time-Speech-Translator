import speech_recognition as sr
import google.generativeai as genai
import os
import pyttsx3 

api_key = os.getenv("API_KEY")
if not api_key:
    print("Error: API_KEY environment variable not set.")
    print("Please set your API key in your terminal.")
    exit()
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash') 
r = sr.Recognizer()

def translate_and_speak(recognizer, model): 
    with sr.Microphone() as source:
        print("\nSpeak in Tamil now...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("No speech detected within the time limit.")
            return
        
    try:
        tamil_text = recognizer.recognize_google(audio, language="ta-IN")
        print(f"[Source Tamil Text]: {tamil_text}\n")
    except sr.UnknownValueError:
        print("\nCould not understand audio (STT did not recognize speech).")
        return
    except sr.RequestError as e:
        print(f"\nCould not request results from Speech Recognition service; {e}")
        return
    
    try:
        print("Translating...\n")
        prompt = f"Please translate the following Tamil text into English. Provide only the translated English text and nothing else.\n\nTamil: \"{tamil_text}\"\nEnglish:"
        response = model.generate_content(prompt)
        translated_text = response.text.strip()
        print(f"[Translated English Text]:\n{translated_text}")
    except Exception as e:
        print(f"\nAn error occurred during translation: {e}")
        print("Please check your API_KEY, internet connection.")
        return

    if translated_text:
        try:
            print("Speaking translation...")
            tts_engine = pyttsx3.init() 
            tts_engine.say(translated_text)
            tts_engine.runAndWait()
        except Exception as e:
            print(f"\nAn error occurred during text-to-speech: {e}")
    else:
        print("Translation was empty, nothing to speak.")

if __name__ == '__main__':
    print("--- Tamil to English Voice Translator ---")
    while True:
        user_input = input("\nAre you ready to speak? (Enter '1' to start, '0' to exit): ").strip().lower()
        if user_input == '0':
            print("Exiting translator")
            break 
        elif user_input == '1':
            translate_and_speak(r, model) # DELETED: tts_engine
        else:
            print("Invalid input. Please enter '1' or '0'.")
            
