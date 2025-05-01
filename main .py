import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog



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
        
        
        
