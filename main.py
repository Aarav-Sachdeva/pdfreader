from gtts import gTTS
from mutagen.mp3 import MP3
import PyPDF2
import os.path
from replit import audio
import time
from tkinter.filedialog import askopenfilename

reader=askopenfilename()
pdfreader= PyPDF2.PdfFileReader(reader)
pages=pdfreader.numPages
pages=pdfreader.getPage(pages-1)
tex=pages.extractText()
tts=gTTS(text=tex,lang='en')
tts.save('ats.mp3')
audios = MP3("ats.mp3")
duration=audios.info.length
if os.path.isfile('ats.mp3'):
  audio.play_file("ats.mp3")
  time.sleep(duration)