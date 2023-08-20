import speech_recognition as sr
from translate import Translator
from gtts import gTTS
import playsound

file = open('c:\\speaktranslate\lc.csv')
f = file.read()
f = f.split('\n')


def language_select():
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
	    print("what language...")
	    audio = recognizer.listen(source)    
	try:
	    spoken_text = recognizer.recognize_google(audio)
	    print("You said:", spoken_text)
	except sr.UnknownValueError:
	    print("Sorry, could not understand audio.")
	for x in f:
		y = x.split(',')
		if spoken_text==y[1]: return y[0]

def speak(translated_text, sl):
	tts = gTTS(translated_text, lang=sl)
	tts.save('translated_audio.mp3')
	playsound.playsound('translated_audio.mp3')

def translate(spoken_text, sl):
	translator = Translator(to_lang=sl)  # Translate to French
	translated_text = translator.translate(spoken_text)
	print("Translated text:", translated_text)
	return translated_text

def recog():
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Speak something...")
	    audio = recognizer.listen(source)    
	try:
	    spoken_text = recognizer.recognize_google(audio)
	    print("You said:", spoken_text)
	except sr.UnknownValueError:
	    print("Sorry, could not understand audio.")
	return spoken_text

c = language_select()
a = recog()
b=translate(a,c)
speak(b, c)