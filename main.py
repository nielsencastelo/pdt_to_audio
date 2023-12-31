import PyPDF2
from gtts import gTTS
import os
import re

def read_pdf(filename):
    with open(filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ""

        for page_number in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_number)
            text += page.extractText()

        return text
    

def remove_text_before_intro(text):
    # Expressão regular para identificar a seção "Introdução"
    intro_pattern = r"(?i)\bIntrodução\b"

    # Procurar o índice de início da seção "Introdução"
    match = re.search(intro_pattern, text)
    if match:
        start_index = match.start()
        return text[start_index:]
    else:
        return text
    
def remove_references(text):
    # Expressão regular para identificar a seção de "Referências"
    references_pattern = r"(?i)\bReferências\b.*"

    # Remover a seção de "Referências" e todo o texto após ela
    text = re.sub(references_pattern, "", text, flags=re.DOTALL)

    return text

def synthesize_speech(text, output_file):
    tts = gTTS(text, lang="pt-br")
    tts.save(output_file)

    # Reproduzir o arquivo de áudio
    os.system("mpg123 " + output_file)

def remove_header(text, header_text):
    # Remover o cabeçalho do texto
    content = text.replace(header_text, "")
    return content

def main():
    pdf_file = "33674-Article-377528-1-10-20220824.pdf"
    output_file = "output.mp3"
    
    header = """Research, Society and Development, v. 11, n. 1 1, e349111133674 , 2022  
(CC BY 4.0) | ISSN 2525 -3409 | DOI: http://dx.doi.org/10.33448/rsd -v11i11.33674 
    """
    # Ler o PDF
    text = read_pdf(pdf_file)
    text_pre = remove_text_before_intro(text)
    text_pre = remove_references(text_pre)
    text_pre = remove_header(text_pre, header)

    # Sintetizar a voz
    synthesize_speech(text_pre, output_file)

if __name__ == "__main__":
    main()
