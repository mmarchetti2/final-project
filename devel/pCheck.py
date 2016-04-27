import re, sys, os, PyPDF2
def phoneScanner(filename):
    print('You have chosen to search for phone numbers.')
    print('What type of file are you trying to scan?')
    print('\n1. TXT File\n2. PDF')
    ans = input()
    if int(ans) == 1:
        text1 = open(filename + '.txt')
        textContent = text1.read()
        phoneChecker1 = re.compile(r'\d{3}-\d{3}-\d{4}')
        phoneChecker2 = re.compile(r'((\W\d)?\d{10}[\n\s\W])')
        phoneChecker3 = re.compile(r'\(\d{3}\)\s\d{3}-\d{4}')
        mo1 = phoneChecker1.findall(textContent)
        mo2 = phoneChecker2.findall(textContent)
        mo3 = phoneChecker3.findall(textContent)

        print('Form one phone numbers found: ' + str(mo1))
        print('Form two phone numbers found: ' + str(mo2))
        print('Form three phone numbers found: ' + str(mo3))
    elif int(ans) == 2:
        print('Please enter the name of the PDF file you want scanned:')
        fileName = input()
        text1 = open(fileName + '.pdf', 'rb') #Opens the PDF file
        textContent = PyPDF2.PdfFileReader(text1) #Uses the PDF Reader function
        phoneChecker1 = re.compile(r'\d{3}-\d{3}-\d{4}') #Regexes 1-3
        phoneChecker2 = re.compile(r'((\W\d)?\d{10}[\n\s\W])')
        phoneChecker3 = re.compile(r'\(\d{3}\)\s\d{3}-\d{4}')
        pages = 0
        while pages < textContent.numPages: #Uses a loop that starts with page 0, and keeps going until every page is gotten.
            textPage = textContent.getPage(pages)
            mo1 = phoneChecker1.findall(textPage.extractText())
            mo2 = phoneChecker2.findall(textPage.extractText())
            mo3 = phoneChecker3.findall(textPage.extractText())
            pages = pages + 1

        print('Form one phone numbers found: ' + str(mo1))
        print('Form two phone numbers found: ' + str(mo2))
        print('Form three phone numbers found: ' + str(mo3))
    else:
        print('That\'s not a valid number.\nSHUTTING DOWN')
        sys.exit
