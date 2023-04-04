import PyPDF3
import pyttsx3

pdfReader = PyPDF3.PdfFileReader(open('file.pdf', 'rb'))

speaker = pyttsx3.init()

for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female, 0 for male
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

speaker.save_to_file(text, 'audio.mp3')
speaker.runAndWait()