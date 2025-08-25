#**Jarvis Voice Assistant**
**Overview**
Jarvis Voice Assistant is a Python-based desktop voice assistant inspired by the Iron Man AI. It allows users to control their computer using voice commands or text inputs. The assistant can open applications, browse websites, manage WhatsApp interactions (messages, voice calls, video calls), and even handle mobile phone calls and SMS via SIM. Contacts and system app paths are stored in an SQLite database for easy management.
This project uses a combination of speech recognition, text-to-speech, web automation, and database handling to provide a seamless user experience.
**Features**

Voice and Text Command Support: Control your desktop with voice inputs (using a microphone) or typed text commands.
Application Control: Open system apps like Notepad, Chrome, YouTube, or any video streaming website (e.g., "open notepad", "open chrome", "open youtube").
WhatsApp Integration: Send messages, make voice calls, or video calls to any contact in your contact list (e.g., "send message to [contact]", "video call [contact]").
Mobile Phone Control: Make phone calls or send SMS via SIM to contacts (requires appropriate hardware/setup for mobile integration).
Database Management: Uses SQLite3 to store contact lists, website URLs, and system app paths for quick access and customization.
Wake Word Detection: Uses Porcupine (pvporcupine) for hotword detection like "Jarvis" to activate the assistant.
Cross-Platform Compatibility: Primarily tested on Windows, but adaptable to other operating systems with minor changes.

**Technologies Used**

**Python Libraries:**
pyaudio: For audio input/output handling.
pywhatkit: For WhatsApp automation (messages, calls).
playsound: To play audio files.
pyttsx3: Text-to-speech engine for Jarvis's responses.
speech_recognition: For converting voice commands to text.
eel: For creating a simple web-based GUI (using HTML/JS for frontend).
webbrowser: To open websites and apps via browser.
pvporcupine: For wake word/hotword detection.
sqlite3: Built-in Python module for database operations (storing contacts, app paths, etc.).


**Set Up Virtual Environment (Recommended):**
python -m venv .venv
.venv\Scripts\activate  # On Windows
# or source .venv/bin/activate on Unix


**Install Dependencies:Create a requirements.txt file with the following content:**
pyaudio
pywhatkit
playsound
pyttsx3
speechrecognition
eel
pvporcupine



**Database Setup:**

Run db.py to initialize the SQLite database (jarvis.db) for contacts and paths:python db.py


**Run the Assistant:**
python run.py

Say "Jarvis" to wake it up, then give commands like "open chrome" or "send message to Mom".


**Usage**

Voice Commands: Speak clearly into the microphone after the wake word.
Text Inputs: Use the Eel-based web interface to type commands if voice isn't preferred.
Examples:
"Open Notepad"
"Open YouTube"
"Send message to [Contact Name]: Hello!"
"Video call [Contact Name]"
"Call [Phone Number]"



**Video Demo**
Watch the demo video here 

**Acknowledgments**

Inspired by JARVIS from Iron Man.
Thanks to the open-source libraries used in this project.
