import pCheck, cCheck
print('Welcome to mmarchetti2\'s file scanner.')
print('Please choose what you\'d like to scan for:')
print('\n1. Phone Numbers\n2. Four Digit Codes\n3. Times')
ans = input()
if int(ans) == 1:
    print('Please enter the name of the file you\'d like to scan.')
    file = input()
    pCheck.phoneScanner(file)
elif int(ans) == 2:
    print('Please enter the name of the file you\'d like to scan.')
    file = input()
    cCheck.codeScanner(file)
elif int(ans) == 3:
    print('<COMING SOON>')
else:
    print('That\'s not one of the choices...')
    print('<SHUTTING DOWN>')
