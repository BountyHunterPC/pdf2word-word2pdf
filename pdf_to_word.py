from pdf2docx import Converter

pdf = "demo.pdf"
new_word = "new_word.docx"

c = Converter(pdf)
c.convert(new_word)
c.close()