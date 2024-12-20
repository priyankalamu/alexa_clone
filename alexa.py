import speech_recognition as sr  # For speech recognition
from gtts import gTTS  # For text-to-speech
import webbrowser  # To open websites
import threading  # For multi-threading
import os  # To play audio files
import datetime  # To get current time
import random  # For random jokes

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to play text using gTTS
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")  # Play the mp3 file

# Function for listening to voice commands
def listen_for_commands():
    global recognizer
    while True:
        with sr.Microphone() as source:
            print("Listening for commands...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            try:
                audio = recognizer.listen(source, timeout=5)  # Timeout after 5 seconds of silence

                command = recognizer.recognize_google(audio).lower()
                print(f"Command: {command}")

                if 'open google' in command:
                    webbrowser.open('http://www.google.com')
                    speak("Opening Google")

                elif 'open youtube' in command:
                    webbrowser.open('http://www.youtube.com')
                    speak("Opening YouTube")

                elif 'search' in command:
                    query = command.replace("search", "").strip()
                    webbrowser.open(f"http://www.google.com/search?q={query}")
                    speak(f"Searching for {query}")

                elif 'tell the time' in command:
                    current_time = datetime.datetime.now().strftime("%H:%M")
                    speak(f"The current time is {current_time}")

                elif 'tell a joke' in command:
                    jokes = [
                        "Why don't skeletons fight each other? They don't have the guts!",
                        "I told my wife she was drawing her eyebrows too high. She looked surprised!",
                        "What do you call fake spaghetti? An impasta!"
                    ]
                    joke = random.choice(jokes)
                    speak(joke)

                elif 'stop' in command:
                    speak("Goodbye!")
                    break

                else:
                    speak("Sorry, I didn't understand that.")

            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as ex:
                print(f"Error: {ex}")

# Start listening in a separate thread
command_thread = threading.Thread(target=listen_for_commands)
command_thread.daemon = True
command_thread.start()

# Keep the program running with an input prompt
input("Press Enter to stop the program.")
