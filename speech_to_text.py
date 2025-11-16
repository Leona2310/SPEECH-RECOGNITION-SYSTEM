# speech_to_text.py

import speech_recognition as sr

# Create a recognizer object
recognizer = sr.Recognizer()

# Load your audio file
audio_file = "sample.wav"  # Replace with your audio filename

# Open the audio file and recognize speech
with sr.AudioFile(audio_file) as source:
    print("Listening to the audio...")
    audio_data = recognizer.record(source)
    print("Recognizing...")

    try:
        # Use Google's speech recognition
        text = recognizer.recognize_google(audio_data)
        print("\nTranscribed Text:\n")
        print(text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Network error. Please check your internet connection.")
