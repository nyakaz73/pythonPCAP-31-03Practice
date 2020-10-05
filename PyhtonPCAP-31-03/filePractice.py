try:
    x = open('testfile.txt','r')
except FileNotFoundError:
    print('File Not found')

