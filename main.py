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
            print("Recognized speech:", said)

            # Check if the word "Orange" is recognized in speech
            if "Orange" in said: # Cahnged due to it being a more recognisible word
                words = said.split()
                new_string = ' '.join(words[1:])
                print("Filtered string:", new_string)

                # Generate a response using OpenAI
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": said}]
                )
                text = completion.choices[0].message.content
                print("OpenAI response:", text)

                # Convert the response to speech
                speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                speech.save("welcome1.mp3")

                playsound.playsound("welcome1.mp3")

        except Exception as e:
            print("Exception occurred:", str(e))

        return said

# Start an infinite loop
while True:
    # Call the get_audio() function and update the "guy" variable
    guy = get_audio()

    # Check if the word "stop" is being used in the voice
    if "stop" in guy:
        break  # Exit the loop if the word "stop" is heard
