import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        transcription = recognizer.recognize_google(audio)
        return transcription
    except sr.RequestError:
        # API was unreachable or unresponsive
        return "API unavailable"
    except sr.UnknownValueError:
        # Speech was unintelligible
        return "Unable to recognize speech"
