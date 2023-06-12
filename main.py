import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr

api_key = "my_api_key"
lang = 'en'

openai.api_key = api_key

# Start an infinite loop
while True:
    # Function to get audio input
    def get_audio():
        r = sr.Recognizer()
        # Specifies which microphone to use
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            said = ""

            try:
                # Speech recognition on the audio
                said = r.recognize_google(audio)
                print(said)

                # Check if the word "Bobby" is recognised in through in speech
                if "Bobby" in said:
                    words = said.split()
                    new_string = ' '.join(words[1:])
                    print(new_string)

                    # Generate a response using OpenAI
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                              messages=[{"role": "user", "content": said}])
                    text = completion.choices[0].message.content

                    # Convert the response to speech
                    speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                    speech.save("welcome1.mp3")

                    playsound.playsound("welcome1.mp3")

            # Handles Exceptions
            except Exception:
                print("Exception")

            return said

    # Check if the word "stop" is being used in the voice
    if "stop" in guy:
        break  # Exit the loop if the word "stop" is heard

    get_adio()
