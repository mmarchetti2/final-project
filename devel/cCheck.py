import re, sys, os, PyPDF2
def codeScanner(filename):
    print('You have chosen to search for four-digit codes.')
    print('What type of file are you trying to scan?')
    print('\n1. TXT File\n2. PDF')
    ans = input()
    if int(ans) == 1:
        text1 = open(filename + '.txt')
        textContent = text1.read()
        codeChecker = re.compile(r'\s\d{4}\s')
        mo1 = codeChecker.findall(textContent)
        print('Four-digit codes found: ' + str(mo1))
        
    elif int(ans) == 2:
        print('Please enter the name of the PDF file you want scanned:')
        fileName = input()
        text1 = open(fileName + '.pdf', 'rb') #Opens the PDF file
        textContent = PyPDF2.PdfFileReader(text1) #Uses the PDF Reader function
        codeChecker = re.compile(r'\s\d{4}\s')
        pages = 0
        while pages < textContent.numPages: #Uses a loop that starts with page 0, and keeps going until every page is gotten.
            textPage = textContent.getPage(pages)
            mo1 = codeChecker.findall(textPage.extractText())
            pages = pages + 1
        print('Four-digit codes found: ' + str(mo1))
        
    else:
        print('That\'s not a valid number.\nSHUTTING DOWN')
        sys.exit
