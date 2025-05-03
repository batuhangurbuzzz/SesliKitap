import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog
# Functions
def extractPDFText(pdfFile):
    text = ""
    
    pdfReader = PyPDF2.PdfReader(open(pdfFile,'rb'))
    
    for pageNum in range(len(pdfReader.pages)):
        text += pdfReader.pages[pageNum].extract_text()
    return text
     
    
def turnIntoSound(text, soundFile):
    soundTranslate = gTTS(text=text, lang='tr')
    soundTranslate.save(soundFile)
      

def fileSelect():
    filePath = filedialog.askopenfilename(filetypes=[("PDF Dosyaları", "*pdf")])
    if filePath:
        pdfText = extractPDFText(filePath)
        
        turnIntoSound(pdfText,"kaydet.mp3")
        
        os.system("start kaydet.mp3")
        
# Design
app = tk.Tk()
app.title("Sesli Kitap Uygulaması")
app.geometry("250x150")


button = tk.Button(app, text="PDF Seç", command=fileSelect, padx=20, pady=20)

button.pack(pady=20)




app.mainloop()
        
