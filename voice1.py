# importing speech recognition package from google api
import speech_recognition as sr
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open files
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
num = 1
import webbrowser
def assistant_speaks(output):
	global num

	# num to rename every audio file
	# with different name to remove ambiguity
	num += 1
	print("PerSon : ", output)

	toSpeak = gTTS(text = output, lang ='en', slow = False)
	# saving the audio file given by google text to speech
	file = str(num)+".mp3 "
	toSpeak.save(file)

	# playsound package is used to play the same file.
	playsound.playsound(file, True)
	os.remove(file)



def get_audio():

	rObject = sr.Recognizer()
	audio = ''

	with sr.Microphone() as source:
		print("Speak...")

		# recording the audio using speech recognition
		audio = rObject.listen(source, phrase_time_limit = 5)
	print("Stop.") # limit 5 secs

	try:

		text = rObject.recognize_google(audio, language ='en-US')
		print("You : ", text)
		return text

	except:

		assistant_speaks("Could not understand your audio, PLease try again !")
		return 0
                                





def search_web(input_value):
        
	driver = webdriver.Chrome()
	driver.implicitly_wait(1)
	driver.maximize_window()
	if 'youtube' in input_value.lower():
		assistant_speaks("Opening in youtube")
		indx = input_value.lower().split().index('youtube')
		query = input_value.split()[indx + 1:]
		webbrowser.open_new_tab("http://www.youtube.com/results?search_query =" + '+'.join(query))
		return
                
	elif 'wikipedia' in input_value.lower():

		assistant_speaks("Opening Wikipedia")
		indx = input_value.lower().split().index('wikipedia')
		query = input_value.split()[indx + 1:]
		webbrowser.open_new_tab("https://en.wikipedia.org/wiki/" + '_'.join(query))
		return

	else:

		if 'google' in input_value:
                        
			indx = input_value.lower().split().index('google')
			query = input_value.split()[indx + 1:]
			webbrowser.open_new_tab("https://www.google.com/search?q =" + '+'.join(query))

		elif 'search' in input_value:

			indx = input_value.lower().split().index('google')
			query = input_value.split()[indx + 1:]
			webbrowser.open_new_tab("https://www.google.com/search?q =" + '+'.join(query))
                
		else:

			webbrowser.open_new_tab("https://www.google.com/search?q =" + '+'.join(input_value.split()))
                        
		return
                



def open_application(input): 
  
        if "chrome" in input: 
                assistant_speaks("Google Chrome") 
                os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
                return
  
        elif "firefox" in input or "mozilla" in input: 
                assistant_speaks("Opening Mozilla Firefox") 
                os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe') 
                return
  
        elif "word" in input: 
                assistant_speaks("Opening Microsoft Word") 
                os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk') 
                return
  
        elif "excel" in input: 
                assistant_speaks("Opening Microsoft Excel") 
                os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk') 
                return
  
        else: 
  
                assistant_speaks("Application not available") 
                return










def process_text(input_value):
	print(input_value.lower())
	try:
		if 'search' in input_value.lower() or 'play' in input_value.lower():
			search_web(input_value)
			return
		elif "who are you" in input_value.lower() or "define yourself" in input_value.lower(): 
			speak = '''Hello, I am Person. Your personal Assistant.
			I am here to make your life easier. You can command me to perform
			various tasks such as calculating sums or opening applications etcetra'''
			assistant_speaks(speak)
			return (input_value)

		elif "who made you" in input_value.lower() or "created you" in input_value.lower():
			speak = "I have been created by coders."
			assistant_speaks(speak)
			return (input_value)


		elif "calculate" in input_value.lower():

			# write your wolframalpha app_id here
			app_id = "WOLFRAMALPHA_APP_ID"
			client = wolframalpha.Client(app_id)

			indx = input_value.lower().split().index('calculate')
			query = input_value.split()[indx + 1:]
			res = client.query(' '.join(query))
			answer = next(res.results).text
			assistant_speaks("The answer is " + answer)
			return

		elif 'open' in input_value:

			# another function to open
			# different application availaible
			open_application(input_value.lower())
			return

		else:

			assistant_speaks("I can search the web for you, Do you want to continue?")
			ans = get_audio()
			if 'yes' in str(ans) or 'yeah' in str(ans):
				search_web(input_value)
			else:
				return
	except :

		assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?") 
		ans = get_audio() 
		if 'yes' in str(ans) or 'yeah' in str(ans): 
			search_web(input) 

if __name__ == "__main__": 
        assistant_speaks("What's your name ?") 
        name ='Human'
        name = get_audio() 
        assistant_speaks("Hello, " + name + '.') 
      
        while(1): 
  
                assistant_speaks("What can i do for you?") 
                text = get_audio().lower() 
  
                if text == 0: 
                        continue
  
                elif "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
                        assistant_speaks("Ok bye, "+ name+'.')
                        break
  
        
                process_text(text) 
