import re, sys, os, PyPDF2
def timeScanner(filename):
    print('You have chosen to search for times.')
    print('What type of file are you trying to scan?')
    print('\n1. TXT File\n2. PDF')
    ans = input()
    if int(ans) == 1:
        text1 = open(filename + '.txt')
        textContent = text1.read()
        timeChecker = re.compile(r'((\d)?\d:\d{2})')
        mo1 = timeChecker.findall(textContent)
        print('Times found: ' + str(mo1))
        
    elif int(ans) == 2:
        print('Please enter the name of the PDF file you want scanned:')
        fileName = input()
        text1 = open(fileName + '.pdf', 'rb') #Opens the PDF file
        textContent = PyPDF2.PdfFileReader(text1) #Uses the PDF Reader function
        timeChecker = re.compile(r'((\d)?\d:\d{2})')
        pages = 0
        while pages < textContent.numPages: #Uses a loop that starts with page 0, and keeps going until every page is gotten.
            textPage = textContent.getPage(pages)
            mo1 = timeChecker.findall(textPage.extractText())
            pages = pages + 1
        print('Times found: ' + str(mo1))
        
    else:
        print('That\'s not a valid number.\nSHUTTING DOWN')
        sys.exit
