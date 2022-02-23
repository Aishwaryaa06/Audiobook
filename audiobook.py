import pyttsx3
import PyPDF2

engine = pyttsx3.init("sapi5")
book = open('sampleaudiobook.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("The total number of pages in pdf is", pages)
speaker = pyttsx3
page = pdfReader.getPage(0)     #list range starts from 0
text = page.extractText()
engine.say(text)
print("But it reads only one page Because the index is 0.")
#engine.say('Just a sample text')
engine.runAndWait()