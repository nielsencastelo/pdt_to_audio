import PyPDF2
from gtts import gTTS
import io
import os

def read_pdf(filename):
    with open(filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ""

        for page_number in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_number)
            text += page.extractText()

        return text

def synthesize_speech(text, output_file):
    tts = gTTS(text)
    tts.save(output_file)

    # Reproduzir o arquivo de áudio
    os.system("mpg123 " + output_file)

def main():
    pdf_file = "caminho/para/o/arquivo.pdf"
    output_file = "output.mp3"

    # Ler o PDF
    text = read_pdf(pdf_file)

    # Sintetizar a voz
    synthesize_speech(text, output_file)

if __name__ == "__main__":
    main()
