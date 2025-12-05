import PyPDF2

pdfName = 'Python\\Text Processing\\asset\\Tutorialspoint2.pdf'
read_pdf = PyPDF2.PdfFileReader(pdfName)

for i in range(read_pdf.getNumPages()):
    page = read_pdf.getPage(i)
    print ('Page No - ' + str(1+read_pdf.getPageNumber(page)))
    page_content = page.extractText()
    print (page_content)
