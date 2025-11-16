# SPEECH-RECOGNITION-SYSTEM

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : LEONA MENDES

*INTERN ID* : CT04DR1252

*DOMAIN NAME* : ARTIFICIAL INTELLIGENCE

*DURATION* : 4 WEEKS 

*MENTOR* : NEELA SANTOSH


# TASK 2 — SPEECH-RECOGNITION-SYSTEM

The second task focused on developing a functional Speech-to-Text system using Python, with the goal of converting spoken audio into written text automatically. This task is part of the broader field of speech recognition, which allows computers to interpret human speech, making interactions with machines more natural and accessible. For this implementation, I used the SpeechRecognition library, one of the most beginner-friendly and widely-used Python libraries for audio transcription. The task required building a simple script that loads an audio file, processes it through a recognizer, and outputs the transcribed text. Using a pre-recorded audio file such as "sample.wav", the system demonstrates how speech recognition works in real-world applications.

The code begins by importing the SpeechRecognition library and initializing a Recognizer() object. This recognizer handles crucial steps such as detecting speech, reducing background noise, and preparing the audio for transcription. Instead of using complex deep learning models like wav2vec2 or Whisper, this task uses Google’s built-in speech recognition engine provided through the SpeechRecognition library. This engine is highly accurate for short audio clips and does not require advanced machine learning knowledge, making it perfect for beginners or rapid prototyping. After the recognizer is created, the script loads the audio file using sr.AudioFile. This method safely opens the audio and converts it into a format ready for analysis.

Inside the with block, the recognizer listens to the audio using recognizer.record(source), which reads the entire file. The program prints “Listening to the audio...” and “Recognizing...” to indicate that the system is actively processing the file. Once the audio is captured, the main function used to convert speech into text is recognizer.recognize_google(audio_data). This sends the audio to Google’s cloud-based speech recognition API, which returns a transcription of whatever was spoken in the audio file. The output is then printed for the user to see. The script includes error handling using try-except blocks to manage cases where the speech is unclear or if there is a network issue. For instance, UnknownValueError is triggered when the audio cannot be understood, while RequestError appears when an internet connection is unavailable.

This task has many real-world applications. Speech-to-text systems are widely used in voice assistants like Siri, Google Assistant, and Alexa. The same technology powers automated subtitles, call-center speech analytics, meeting transcription tools, and voice-controlled devices. In education, students can record lectures and convert them into text for easier studying. In business, professionals use speech recognition to transcribe meetings or interviews rapidly. In healthcare, doctors often dictate medical notes that are converted into written reports. Speech recognition also supports accessibility by helping individuals with disabilities interact with computers using their voice instead of typing.

By completing this task, I gained a strong understanding of how speech recognition works at a practical level. Although the underlying technology is complex, the SpeechRecognition library simplifies the process and allows high-quality transcription with minimal code. This task demonstrates how artificial intelligence can bridge communication between humans and machines, turning spoken language into text efficiently and accurately. It shows how even beginners can create powerful AI-driven tools with just a few lines of Python. Overall, the task successfully illustrates the fundamentals of speech processing and highlights the importance of speech-to-text systems in modern technology.
