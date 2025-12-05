import PyPDF2

pdfName = 'Python\\Text Processing\\asset\\Tutorialspoint.pdf'
read_pdf = PyPDF2.PdfFileReader(pdfName)
page = read_pdf.getPage(0)
page_content = page.extractText()
print (page_content)
